import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pickle
import os
from typing import List
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from utils.build import build_header

data = pd.read_parquet('data/price_cars10k.parquet')

build_header(
    title='Clusterizacao',
    hdr='# METODO DE CLUSTERIZACAO DOS DADOS',
    p='''
        <p> Nessa etapa buscamos encontrar o numero ideal de clusters para obtermos insights com base nesses grupos criados, os grupos sao formados por corelacoes entre as variaveis e separadas em grupos que divergem entre si</p>
    '''
)

target = ''
if target !='':
    columns_drop = ['preco','preco_categoria']
    X_data= data.drop(columns_drop, axis=1).values
    y_data= data[target].values
else:
    columns_drop = ['preco']
    X_data= data.drop(columns_drop, axis=1).values
    y_data = ''

le = LabelEncoder()
columns_categories = []
if target=='':
    tam = len(data.columns)-1
else:
    tam = len(data.columns)-2

for x in range(tam):
    if not((type(X_data[0, x]) == float) or (type(X_data[0, x]) == int)):
        X_data[:, x] = le.fit_transform(X_data[:, x])
        columns_categories.append(x)

scaler = StandardScaler()
X_data = scaler.fit_transform(X_data)


clr = st.sidebar.slider('Escolha a quantidade de Clusters', 0,10,1)

def chart_wcss(x_data):
  wcss = []
  for i in range(1, 11):
    kmeans = KMeans(n_clusters= i , random_state=0)
    kmeans.fit(x_data)
    wcss.append(kmeans.inertia_)
  graph_wcss = px.line(x= range(1,11), y=wcss)
  st.plotly_chart(graph_wcss)
  return wcss

chart_wcss(X_data)


def kmeans(x_data,nclusters:int):

  kmeans = KMeans(n_clusters=nclusters, random_state=0)
  labels = kmeans.fit_predict(x_data)
  pca = PCA(n_components=2)
  X_pca = pca.fit_transform(x_data)
  graph_clusters = px.scatter(x= X_pca[:,0], y= X_pca[:,1], color=labels)
  st.plotly_chart(graph_clusters)

kmeans(X_data, nclusters=clr)



