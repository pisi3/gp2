import pandas as pd
import plotly.express as px
import streamlit as st
import pickle
import numpy as np

import os
from utils.build import build_header
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from utils.transform_pkl import main

def table_report(y_test: np.ndarray, previsao: np.ndarray, method:str =''):
  st.markdown(f'#### Classification report do metodo:  <span style="color: blue">{method}</span>', unsafe_allow_html=True)
  report = classification_report(y_test, previsao, output_dict=True)
  classification_data = pd.DataFrame(report).transpose()
  st.table(classification_data)



def confusion_graph(y_test, previsao, method:str = ''):
  st.markdown(f'#### Matriz de Confução do metodo: <span style="color: blue">{method}</span>', unsafe_allow_html=True)
  labels = sorted(list(set(y_test) | set(previsao)))
  cm = pd.DataFrame(0, index=labels, columns=labels)
  for true_label, predicted_label in zip(y_test, previsao):
      cm.loc[true_label, predicted_label] += 1
  st.table(cm)


def naive_bayes(
  x_training: np.ndarray, y_training: np.ndarray, x_test: np.ndarray, y_test: np.ndarray
  )-> None:

  if not(os.path.isfile('data/naive_bayes.pkl')):
    naive = GaussianNB()
    naive.fit(X_training, y_training)
    with open('data/naive_bayes.pkl', mode='wb') as f:
      pickle.dump(naive, f)
  else:
    with open('data/naive_bayes.pkl', 'rb') as f:
      naive = pickle.load(f)
  previsor = naive.predict(X_test)
  table_report(y_test, previsor, 'Naive Bayes')
  confusion_graph(y_test, previsor, 'Naive Bayes')



if not(os.path.isfile('data/price_cars.pkl')):
  print('iniciando...')
  main()

with open('data/price_cars.pkl', 'rb') as f:
    X_training, X_test, y_training, y_test = pickle.load(f)

    
naive_bayes(X_training, y_training, X_test, y_test)