

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html

import pandas as pd

from components import nav

from app import app

# Dados fictícios para a tabela
df = pd.DataFrame({
   "Nome": ["Ana", "Bruno", "Carlos"],
   "Idade": [25, 30, 22],
   "Profissão": ["Engenheira", "Designer", "Desenvolvedor"]
})

# Criando as linhas da tabela
tabela = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

tabela = dbc.Container(children=[
   tabela
], fluid=True, style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'text-align': 'center','height': '500px' ,'with': '100vh'})
