import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, 'utils')
from build import build_header
from utils.charts import boxplot,scatter,treemap,hist,bar,select_chart, strip
from utils.build import top_categories

data = pd.read_parquet('data\price_cars500k.parquet')
data_group = data.groupby(['preco','marca', 'ano', 'modelo','estado','cidade','quilometragem']).size().reset_index(name='Total')
data_group.sort_values('Total', ascending=True, inplace=True)
#data_cars = data[['ano', 'preco', 'marca', 'modelo','estado','cidade']]
data_mean = data.groupby(['cidade']).agg({'preco':'sum','quilometragem':'mean'})


build_header(

    title='Análise Quilometragem',
    hdr='# Análise quilometragem',
    p='''
        <p> Primeiras analises no dataset de quilometragem</p>
    '''
)

data_filtered= top_categories(
    data=data,
    top= 10,
    label='ano'
)

boxplot(
    data= data_filtered,
    title='BoxPlot do Ano por Quilometragem',
    x='ano',
    y='quilometragem',
    p='''<p style='text-align:justify;'> Escrever aqui a analise do grafico! </p>'''
)


km_preco = data[['preco','quilometragem']]

boxplot(
    km_preco,
    x='quilometragem',
    title='BOXPLOT DOS QUILOMETRAGEM',
    p='Aqui vemos a distribuicao dos precos dos veiculos'
)


scatter(
    data= data,
    x='quilometragem',
    y='preco'
)
scatter(
    data= data,
    x='quilometragem',
    y='ano'
)


treemap(
  data=km_preco, 
  options=data.columns.to_list(),
  default=data.columns.to_list()[:2],
)

#grafico de barras

km_modelo = data.groupby("modelo", as_index=True)[['quilometragem']].mean()
km_modelo.sort_values('quilometragem', ascending=False, inplace=True)
km_modelo = km_modelo.head(10)
bar(
    title='GRAFICO DE BARRAS, MODELO X QUILOMETRAGEM',
    data = km_modelo,
    x='quilometragem'
)


data.sort_values('quilometragem', ascending=True, inplace=True)
select_chart(
  data,
  x = 'quilometragem',
  options = data.columns,
  type_graph=px.bar,
  type_txt='GRAFICO DE BARRAS'
)


strip(
    data_mean,
    x='preco',
    y='quilometragem',
    title='Distribuicao da quilometragem em funcao do preco',
    p='''<p style='text-align:justify;'> Escrever aqui a analise do grafico! </p>'''
)