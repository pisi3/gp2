

import pandas as pd
import plotly.express as px
import streamlit as st
import pickle
import numpy as np

import os
from utils.build import build_header, breakrows
from sklearn.metrics import classification_report
from yellowbrick.classifier import ConfusionMatrix
import streamlit_yellowbrick as sty
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error



data = pd.read_parquet('data/price_cars.parquet')


columns_drop = ['preco','preco_categoria']
# definindo as features e target
def features_and_target(data: pd.DataFrame, target: str, columns_drop):
  X_data= data.drop(columns_drop, axis=1)
  y_data= data[target]
  return X_data, y_data

def standard(x_data):
  scaler = StandardScaler()
  x_data = scaler.fit_transform(x_data)

  return x_data




def pre_processing(data):
  X_data, y_data = features_and_target(data,'preco',columns_drop)
  le=LabelEncoder()
  for col in X_data:
    if X_data[col].dtypes == 'object':
      X_data[col] = pd.DataFrame(le.fit_transform(X_data[col]))

  X_data = X_data.values
  y_data = y_data.values
  X_data = standard(X_data)

  return X_data, y_data

def save_pkl(
  x_data: np.ndarray, y_data: np.ndarray, path: str = 'linear_regressor.pkl', per: int =0.2, random: int=0
  )-> None:
  '''save(x_training, y_training, x_teste, y_teste)'''
  X_training, X_test, y_training, y_test = train_test_split(
  X_data, y_data, test_size=per, random_state=random
    )
  with open(path, mode='wb') as f:
    pickle.dump([X_training, X_test, y_training, y_test], f)

  return X_training, X_test, y_training, y_test

X_data, y_data = pre_processing(data)

def main():
  if not(os.path.isfile('data/linear_regressor.pkl')):
    save_pkl(X_data, y_data,'data/linear_regressor.pkl')
  X_training, X_test, y_training, y_test = save_pkl(X_data, y_data,'linear_regressor.pkl')

main()

with open('data/linear_regressor.pkl', 'rb') as f:
    X_training, X_test, y_training, y_test = pickle.load(f)



def LinearRegressorMultiple(
  x_training: np.ndarray, y_training: np.ndarray, x_test: np.ndarray, y_test: np.ndarray
  )-> None:
  st.markdown('### Resultado do Modelo Regressao Linear Multipla')
  breakrows()
  if not(os.path.isfile('data/price_linear.pkl')):
    obj_linRM = LinearRegression()
    obj_linRM.fit(x_training, y_training)
    with open('data/price_linear.pkl', mode='wb') as f:
      pickle.dump(obj_linRM, f)
  else:
    with open('data/price_linear.pkl', 'rb') as f:
      obj_linRM = pickle.load(f)
  prevision = obj_linRM.predict(x_test)
  intercept = obj_linRM.intercept_
  score_train = obj_linRM.score(x_training, y_training)
  score_test = obj_linRM.score(x_test,y_test)
  mae = mean_absolute_error(y_test, prevision)
  col1, col2, col3 = st.columns(3)
  col1.metric("Parametro b0",round(intercept))
  col2.metric("Score teste",f'{round(score_test*100)}%')
  col3.metric("Mean Absolute Error",round(mae))


LinearRegressorMultiple(X_training, y_training, X_test, y_test)




