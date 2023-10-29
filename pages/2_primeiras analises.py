import streamlit as st
import pandas as pd
from utils.build import build_header
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from utils.charts import boxplot

data = st.session_state["data"]

build_header(
    title='Prinmeiras Analises',
    hdr='# PRIMEIRAS ANALISES E VISUALIZACOES',
    p='''
        <p> Primeiras analises no dataset</p>
    '''
)

boxplot(
    data,
    x='preco',
    title='BOXPLOT DOS PRECOS',
    p='Aqui vemos a distribuicao dos precos dos veiculos'
)


boxplot(
    data,
    x='ano',
    title='BOXPLOT DOS ANOS',
    p='Aqui vemos a distribuicao dos anos dos veiculos'
)

# options = st.multiselect(
#          'What are your favorite colors',
#     ['Green', 'Yellow', 'Red', 'Blue'],
#     ['Yellow', 'Red'])

# st.write('You selected:', options)