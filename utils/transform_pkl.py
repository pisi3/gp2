import pandas as pd
import numpy as np
import pickle
import os

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


df = pd.read_parquet('data\price_cars500k.parquet')
le=LabelEncoder()
df['cidade'] = pd.DataFrame(le.fit_transform(df['cidade']))
df['estado']= pd.DataFrame(le.fit_transform(df['estado']))
df['marca']= pd.DataFrame(le.fit_transform(df['marca']))
df['modelo']= pd.DataFrame(le.fit_transform(df['modelo']))


y_data=df['preco_categoria'].values
X_data=df.drop(['preco','preco_categoria'],axis=1).values

scaler = StandardScaler()
X_data = scaler.fit_transform(X_data)


X_training, X_test, y_training, y_test = train_test_split(X_data, y_data, test_size= 0.2, random_state= 0)