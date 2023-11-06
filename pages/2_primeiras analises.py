import streamlit as st
import pandas as pd
import numpy as np
from utils.build import build_header
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from utils.charts import boxplot,scatter,treemap,hist,bar,select_chart



build_header(
    title='Prinmeiras Analises',
    hdr='# PRIMEIRAS ANALISES E VISUALIZACOES',
    p='''
        <p> Primeiras analises no dataset</p>
    '''
)
data = pd.read_parquet('data\price_cars10k.parquet')

data_preco = data.groupby(['preco','marca', 'ano', 'modelo',]).size().reset_index(name='Total')
data_preco.sort_values('Total', ascending=True, inplace=True)
data_cars = data[['ano', 'preco', 'marca', 'modelo']]

with st.expander("ViSUALIZAR OS DADOS DESTA SEÇÃO"):
    _, c2, _ = st.columns((1,7,1))
    c2.write(data_cars)



boxplot(
    data,
    x='preco',
    title='BOXPLOT DOS PRECOS',
    p='Aqui vemos a distribuicao dos precos dos veiculos'
)


scatter(
    data= data,
    x='preco',
    y='quilometragem'
)


treemap(
  data=data_preco, 
  options=data.columns.to_list(),
  default=data.columns.to_list()[:2],
)


hist(
    data = data,
    x='marca'
)



#grafico de barras
data_ano = data.groupby(['ano'])['preco'].size().reset_index()
bar(
    title='GRAFICO DE BARRAS, PRECO X ANO',
    data = data_ano,
    x='ano',
    y='preco'
)





select_chart(
  data,
  x = 'marca',
  options = data.columns,
  type_graph=px.bar,
  type_txt='GRAFICO DE BARRAS'
)
