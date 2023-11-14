import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, 'utils')
from build import build_header
from charts import boxplot,scatter,treemap,hist,bar,select_chart

build_header(

    title='Análise Quilometragem',
    hdr='# Análise quilometragem',
    p='''
        <p> Primeiras analises no dataset de quilometragem</p>
    '''
)
data = pd.read_parquet('data\price_cars10k.parquet')
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