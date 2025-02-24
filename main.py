# main
import pandas as pd
df = read_csv("data/uber_data.csv")

df.head()
df.info()

df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

df.info()

datetime_dim = df[['tpep_pickup_datetime', 'tpep_dropoff_datetime']].drop_duplicates().reset_index(drop=True)
datetime_dim['pick_hour'] = datetime_dim['tpep_pickup_datetime'].dt.hour
datetime_dim['pick_day'] = datetime_dim['tpep_pickup_datetime'].dt.day
datetime_dim['pick_month'] = datetime_dim['tpep_pickup_datetime'].dt.month
datetime_dim['pick_year'] = datetime_dim['tpep_pickup_datetime'].dt.year
datetime_dim['pick_weekend'] = datetime_dim['tpep_pickup_datetime'].dt.weekend

datetime_dim['drop_hour'] = datetime_dim['tpep_pickup_datetime'].dt.hour
datetime_dim['drop_day'] = datetime_dim['tpep_pickup_datetime'].dt.day
datetime_dim['drop_month'] = datetime_dim['tpep_pickup_datetime'].dt.month
datetime_dim['drop_year'] = datetime_dim['tpep_pickup_datetime'].dt.year
datetime_dim['drop_weekend'] = datetime_dim['tpep_pickup_datetime'].dt.weekend

datetime_dim['datetime_id'] = datetime_dim.index
