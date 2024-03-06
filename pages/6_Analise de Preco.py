import streamlit as st
import pandas as pd
import numpy as np
from utils.build import build_header
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from utils.charts import boxplot,scatter,treemap,hist,bar,select_chart
from utils.build import breakrows,top_categories


build_header(
    title='Analise de preco',
    hdr='# Analise de preço dos Veiculos',
    p='''
        <p> Nessa analise  buscamos entender onde a influencia do ano do veiculo e quais regioes temos a maior concetração de veiculos  e marcas </p>
    '''
)

data = pd.read_parquet('data\price_cars10k.parquet')
st.write(data.head())

data_preco = data.groupby(['preco','marca', 'ano', 'modelo','estado','cidade']).size().reset_index(name='Total')
data_preco.sort_values('Total', ascending=True, inplace=True)
data_cars = data[['ano', 'preco', 'marca', 'modelo']]

with st.expander("ViSUALIZAR OS DADOS DESTA SEÇÃO"):
    _, c2, _ = st.columns((1,7,1))
    c2.write(data_cars)

breakrows()


data_filtered= top_categories(
    data=data,
    top= 10,
    label='modelo'
)
breakrows()
boxplot(
    data= data_filtered,
    title='BoxPlot do Modelo por Preco',
    x='modelo',
    y='preco',
    p='''<p style='text-align:justify;'>  </p>'''
)




boxplot(
    data_preco,
    x='preco',
    title='BOXPLOT DOS PRECOS',
    p='''Nesse boxplot  vemos a distribuicao dos precos dos veiculos , 
    temos uma concentração maior de veiculos entre 13 mil e 26 mil reais.''')

breakrows()

scatter(
    data= data_filtered,
    x='preco',
    title='Scatter do Preço pela Quilometragem',
    y='quilometragem',
    p='''vemos a relação entre o preço e a quilometragem rodada do veiculo,
      os veiculos com maior quilometragem tendem a ter o valor menor, 
      podemos considerar uma correlação negativa entre essas variaveis, 
      mas temos que levar em conta outras variaveis pois a correlação nao implica causalidade,
        o ano e modelo sao deterministico na precificação final'''
)

treemap(
  data=data_preco, 
  options=data.columns.to_list(),
  default=data.columns.to_list()[:2],
)
