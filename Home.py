import streamlit as st
import pandas as pd


st.set_page_config(
        page_title='Home',
        initial_sidebar_state='expanded',
    )
st.header('Predicao e Analise de dados com Machine Learning')
st.write('''<p> Nesse projeto, buscou-se analisar as caracteriscas corporais e 
            clinicas para realizar previsao se um determinada pessoas e fumante,
            ja foi fumante e parou ou se nunca fumou, tambem podemos
            identificar com essas mesmas caracteristicas se essa mesma pessoa consome bebida alccolica(bebe) ou nao </p>
    ''', unsafe_allow_html=True)

if "data" not in st.session_state:
    data = pd.read_parquet('data\smoking_drinking500k.parquet')
    st.session_state["data"]=data


st.markdown(f'''
    Iremos realizar diversas analises buscando entender correlações entre altura , peso , cintura e idade com o fato da pessoa ser fuamante, alguns dados clinicos como colesterol apresenta alteração em pessoas que bebe e fuma, esses dados serao cruciais para seja possivel determinar se a pessoa ja consumiu bebida , ou é fumante.
            
    <br>
    Passo a Passo desse projeto:
    <ul>
            <li>Exploração e visualização dos dados</li>
            <li>Analise Exploratoria</li>
            <li>Tratamento dos dados para uso dos algoritimos ML</li>
            <li>Aplicação de Marchine Learning</li>
            <li>Metricas</li>
            <li>Comparando modelos</li>
    </ul>
    Dataset: <a href="https://www.kaggle.com/datasets/sooyoungher/smoking-drinking-dataset">https://www.kaggle.com/datasets/sooyoungher/smoking-drinking-dataset</a><br>
    Contribuidores:<br>Silas Ribeiro<br> Vitor Simplicio<br> Edniz Leandro<br>
''', unsafe_allow_html=True)
