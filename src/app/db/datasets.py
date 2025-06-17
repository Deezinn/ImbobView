import pandas as pd
import sqlite3
from db.connect import engine

query_ipca = 'SELECT * FROM ipca_dados'
query_sinapi = 'SELECT * FROM sinapi_dados'

with sqlite3.connect("dados_local.sqlite") as conn:
   pd.read_sql(query_ipca, engine).to_sql("ipca_dados", conn, if_exists="replace", index=False)
   pd.read_sql(query_sinapi, engine).to_sql("sinapi_dados", conn, if_exists="replace", index=False)

   ipca_df = pd.read_sql("SELECT * FROM ipca_dados", conn)
   sinapi_df = pd.read_sql("SELECT * FROM sinapi_dados", conn)
