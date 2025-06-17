import pandas as pd
from db.connect import engine

query_ipca = 'SELECT * FROM ipca_dados ORDER BY periodo DESC LIMIT 10'
query_sinapi = 'SELECT * FROM sinapi_dados ORDER BY periodo DESC LIMIT 10'

ipca_df = pd.read_sql(query_ipca, engine)
sinapi_df = pd.read_sql(query_sinapi, engine)
