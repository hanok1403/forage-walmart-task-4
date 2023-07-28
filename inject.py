import numpy as np
import pandas as pd
import sqlite3

conn = sqlite3.connect('shipment_database.db')

# Read data from the CSV files into pandas DataFrames
s1 = pd.read_csv('data\\shipping_data_0.csv')
s2 = pd.read_csv('data\\shipping_data_1.csv')
s3 = pd.read_csv('data\\shipping_data_2.csv')

conn.execute('select * from shipment_database')

s1.to_sql('shipment_database', conn, if_exists='append', index=False)
s2.to_sql('shipment_database', conn, if_exists='append', index=False)
s3.to_sql('shipment_database', conn, if_exists='append', index=False)



conn.commit()
conn.close()

