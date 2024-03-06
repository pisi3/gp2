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
from utils.build import top_categories, breakrows

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

data_filtered2= top_categories(
    data=data,
    top= 10,
    label='modelo'
)

boxplot(
    data= data_filtered,
    title='BoxPlot do Ano por Quilometragem',
    x='ano',
    y='quilometragem',
    p='''<p style='text-align:justify;'> Existe uma variação de tendencia natural do ano  em relação a quilometragem, o que era de se esperar carros mais antigos tem uma concetração maior entre 100k a 140k quilometros, carros de 2016 por exemplo se concentram abaixo dos 40k .  </p>'''
)


km_preco = data[['preco','quilometragem']]

boxplot(
    km_preco,
    x='quilometragem',
    title='BOXPLOT DOS QUILOMETRAGEM',
    p='Aqui vemos a distribuicao dos precos dos veiculos'
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
    data = data_filtered2,
    x='modelo'
)


data.sort_values('quilometragem', ascending=True, inplace=True)
select_chart(
  data,
  x = 'quilometragem',
  options = data.columns,
  type_graph=px.bar,
  type_txt='GRAFICO DE BARRAS'
)


breakrows()

boxplot(
    data= data_filtered,
    title='BoxPlot do Modelo por Preco',
    x='modelo',
    y='preco',
    p='''<p style='text-align:justify;'>  </p>'''
)



strip(
    data_mean,
    x='preco',
    y='quilometragem',
    title='Distribuicao da quilometragem em função do preço',
    p='''<p style='text-align:justify;'> Nesse grafico é possivel identificar uma concentração maior de veiculos até 20k e com quilometragem entre 20k e 65k, isso permite ofertar de acordo com quantidade de veiculos nessa faixa de valores e quiloemtros rodados </p>'''
)