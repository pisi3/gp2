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
    hdr='# Analise por Quilometragem',
    p='''
        <p> Com base na quantidade de quilometragem do veiculos , buscamos identificar correlação entre essa variavel e o ano do veiculo , preco e outras variaveis</p>
    '''
)


data = pd.read_parquet('data\price_cars10k.parquet')

data = data.groupby(['preco','marca', 'ano', 'modelo','estado','cidade','quilometragem']).size().reset_index(name='Total')
data.sort_values('Total', ascending=True, inplace=True)
data_cars = data[['ano', 'preco', 'marca', 'modelo','quilometragem']]

with st.expander("ViSUALIZAR OS DADOS DESTA SEÇÃO"):
    _, c2, _ = st.columns((1,7,1))
    c2.write(data_cars)

breakrows()

boxplot(
    data=data,
    title='Boxplot Quilometragem',
    x='quilometragem',
    p='''<p> Podemos observar que os veiculos tem maior concentracao entre 23k e 71k quilometros rodados</p>
'''
)


bar(
    data=data,
    x='ano',
    y='quilometragem'
)


scatter(
    data=data,
    x='quilometragem',
    y='preco'
)


data_filtered= top_categories(
    data=data,
    top= 10,
    label='ano'
)
breakrows()
boxplot(
    data= data_filtered,
    title='BoxPlot da Marca por Quilometragem',
    x='ano',
    y='quilometragem',
    p='''<p style='text-align:justify;'>  </p>'''
)
