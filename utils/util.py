import pandas as pd
import numpy as np
import os

def load_dataset(path: str):

    data = pd.read_csv(path)
    return data


datadir = os.getcwd().strip('utils') + 'data'
df = load_dataset(datadir +'\price_cars.csv')
#duplicatas

df.drop_duplicates(keep='first')
df = df.drop('Vin', axis=1)
df.rename(columns={'Price': 'preco','Year': 'ano','Mileage': 'quilometragem','City': 'cidade', 'State': 'estado', 'Make': 'marca', 'Model': 'modelo'}, inplace = True)
df['modelo'] = df['modelo'].replace(['1','2','3','4','5','6','7','8'], ['Serie 1','Serie 2','Serie 3','Serie 4','Serie 5','Serie 6','Serie 7','Serie 8'])


list_outliers = ['preco','ano','quilometragem']
def drop_outliers(df, columns, k=1.5):
    for column in columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        df[column] = df[column].clip(lower=q1 - k * iqr, upper=q3 + k * iqr)
    return df
drop_outliers(df,list_outliers,k=1.5)


def transform_parquet(path, engine='auto'):
  path = path
  try:
    new_data = df.to_parquet(path)
    print('successful')
  except:
    print('error')
  return new_data

transform_parquet(datadir + '\price_cars.parquet')


def random_parquet(path: str, num: int) ->None:
  data = pd.read_parquet(path)
  new_data = data.sample(num, replace=False)
  num2 = ''.join(reversed(''.join(reversed(f'{num}')).replace('000','k')))
  new_data.to_parquet(path.replace('.',f'{num2}.'))

for i in [10000,100000,500000]:
  random_parquet(datadir + '\price_cars.parquet',i)
