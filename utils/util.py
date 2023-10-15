import pandas as pd
import numpy as np


def load_dataset(path: str):

    data = pd.read_csv(path)
    return data
df = load_dataset('gp2\data\smoking_drinking.csv')
#duplicatas
df[df.duplicated].shape

df = df.drop_duplicates(keep='first')
df[df.duplicated].shape


list_outliers = ['age','height','weight','waistline','sight_left','sight_right','hear_left','hear_right','SBP','DBP','BLDS','tot_chole','HDL_chole','LDL_chole','triglyceride','hemoglobin','urine_protein','serum_creatinine','SGOT_AST','SGOT_ALT','gamma_GTP']
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

transform_parquet('gp2\data\smoking_drinking.parquet')


def random_parquet(path: str, num: int) ->None:
  data = pd.read_parquet(path)
  new_data = data.sample(num, replace=False)
  num2 = ''.join(reversed(''.join(reversed(f'{num}')).replace('000','k')))
  new_data.to_parquet(path.replace('.',f'{num2}.'))

for i in [100000,500000]:
  random_parquet('gp2\data\smoking_drinking.parquet',i)