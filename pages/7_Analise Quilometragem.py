import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

sys.path.insert(1, 'utils')
from utils.build import build_header, top_categories
from utils.charts import bar, boxplot, hist, scatter, select_chart, treemap

build_header(

    title='Análise Quilometragem',
    hdr='# Análise quilometragem',
    p='''
        <p> Primeiras analises no dataset de quilometragem</p>
    '''
)
data = pd.read_parquet('data\price_cars10k.parquet')

km_preco = data[['preco','quilometragem']]

data_filtered= top_categories(
    data=data,
    top= 10,
    label='modelo'
)

boxplot(
    km_preco,
    x='quilometragem',
    title='BOXPLOT DOS QUILOMETRAGEM',
    p='''Aqui podemos ver a distribuição da quilometragem dos veículos. 
    A maior concentração de registros está entre 24 mil e 73 mil quilometros. Sendo a metade numa faixa de até 40 mil, e a outra metade de 40 mil a aproximadamente 140 mil.
    '''
)
boxplot(
    data= data_filtered,
    title='BoxPlot do Modelo por Preco',
    x='modelo',
    y='quilometragem',
    p='''<p style='text-align:justify;'>  </p>'''
)


scatter(
    data= data_filtered,
    x='quilometragem',
    y='modelo'
    
)
scatter(
    data= data,
    x='ano',
    y='quilometragem',
    p = '''Esse gráfico mostra a dispersão dos valores da quilometragem de acordo com o ano de fabricação do veículo,
    como podemos observar para modelos mais antigos até o ano de 2009 são encontrados poucos registros numa faixa abaixo dos 20 mil quilometros rodados. 
    Para os anos apartir de 2015 nota-se que poucos são os registros com quilometragem acima de 100 mil quilometros.''',
)


hist(data =  data, x = 'ano', y = 'quilometragem', title = 'histograma',
      p = '''Aqui observamos o histograma com o somatório das quilometragens por ano de fabricação.
      Nota-se que é um histograma bimodal, apresentando dois picos, e com alta variação nas frequências dos dados''')

#Gráfico de barras

variavel_selecionada = st.selectbox('Selecione a variável para o eixo x', ['ano', 'marca', 'estado'])

if variavel_selecionada == 'ano':
    km_grouped = data.groupby("ano", as_index=True)[['quilometragem']].mean()
    title = 'GRAFICO DE BARRAS QUILOMETRAGEM MÉDIA X ANO'
    x_axis_range = list(range(2004, 2024))  # Lista de anos de 2005 a 2023
    descricao = '''Podemos ver no gráfico abaixo que assim como esperado os veículos com ano de fabricação mais antigo possuem maiores médias de quilometros rodados, quanto mais novo o carro menor a média de rodagem'''

elif variavel_selecionada == 'marca':
    km_grouped = data_filtered.groupby("marca", as_index=True)[['quilometragem']].mean()
    title = 'GRAFICO DE BARRAS QUILOMETRAGEM MÉDIA X MARCA'
    descricao = '''Ao analisarmos as quilometragens médias dentre as marcas com maiores médias de quilometragem 
     podemos observar uma certa discrepância entre as marcas "Pontiac" e "Mercury", em relação as demais,
      cujas médias estão acerca de 50 a 60 mil acima do restante das marcas.
    Isso se deve ao fato destas marcas serem mais antigas que inclusive já sairam de linha. Corroborando o que foi observado no gráfico Km x Ano'''
else: 
    km_grouped = data_filtered.groupby("estado", as_index=True)[['quilometragem']].mean()
    title = 'GRAFICO DE BARRAS QUILOMETRAGEM MÉDIA X ESTADO'
    descricao = '''Dentre os registros com maiores médias de quilometragem, podemos observar pelo gráfico a seguir
    uma distribuição bastante uniforme, com três estados se destacando, apresentando maiores médias, são estes
      "Vermont", "Dakota do Norte" e "Wyoming". Os três estão entre os estados com menor PIB nos Estados Unidos, na primeira, segunda e quarta posição, respectivamente.
          O que indica que por possuir menor poder de compra, a população tende a optar pela aquisição de veículos usados '''

km_grouped.sort_values('quilometragem', ascending=False, inplace=True)
km_grouped = km_grouped.head(10)

#criado gráfico
fig = px.bar(
    km_grouped,
    y= 'quilometragem',
    title= title,
    
)

if variavel_selecionada == 'ano':
    fig.update_xaxes(tickvals=x_axis_range, ticktext=x_axis_range)

st.markdown(descricao)

st.plotly_chart(fig)