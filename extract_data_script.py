import requests
from pandas.io.json import json_normalize
import pandas as pd

# Ligar ao JSON

url = 'http://opendata-cml.qart.pt:8080/lastmeasurements'
df = pd.read_json(url, dtype = {"date": int})
df['date'] = df['date'].astype(str)
df['date_modified'] = df['date'].map(lambda x: x[:-6])
df['date_modified'] = pd.to_datetime(df['date_modified'], format='%Y%m%d%H%M')

df['acronimo_short'] = df['id'].map(lambda x: x[:4])

# Get today date now to file name when export to csv or excel with encoding utf8
from datetime import datetime
df.to_csv(datetime.now().strftime('../data_sources/output/parametros_ambientais-%Y-%m-%d-%H-%M-%S.csv'), encoding='utf8')
