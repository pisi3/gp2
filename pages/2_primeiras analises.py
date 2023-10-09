import streamlit as st
import pandas as pd
from utils.build import build_header

data = st.session_state["data"]

build_header(
    title='Prinmeiras Analises',
    hdr='# PRIMEIRAS ANALISES E VISUALIZACOES',
    p='''
        <p> Primeiras analises no dataset</p>
    '''
)

ages = data['age'].unique()
sexs = data['sex'].unique()
drks = data['DRK_YN'].unique()
smks = data['SMK_stat_type_cd'].unique()

age = st.sidebar.selectbox("Idade", ages)
sex = st.sidebar.selectbox("Sexo", sexs)
drk = st.sidebar.selectbox("Comsome Bebida?", drks)
smk = st.sidebar.selectbox("Fumante:", smks)





