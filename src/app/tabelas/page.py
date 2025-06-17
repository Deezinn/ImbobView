import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import Input, Output, State, dcc, html

from components import nav
from db.datasets import ipca_df, sinapi_df
from app import app

tabela = dbc.Container([

   html.H1("Visualização de Dados Econômicos", className="text-center my-4 fw-bold"),

   dbc.Row([
      dbc.Col([
         dbc.Button("Alternar para SINAPI", id="botao-alternar", color="primary", className="mb-4", style={'justify-content': 'center', 'align-items': 'center', 'text-align': 'center'}),
         html.Div(id="container-tabela", style={'justify-content': 'center', 'align-items': 'center', 'text-align': 'center'})
      ], width=12),
   ], style={'justify-content': 'center', 'align-items': 'center', 'text-align': 'center'}),

], fluid=True, className="bg-light p-4")

@app.callback(
   Output("container-tabela", "children"),
   Output("botao-alternar", "children"),
   Input("botao-alternar", "n_clicks"),
   prevent_initial_call=False
)
def alternar_tabela(n_clicks):
   if n_clicks is None or n_clicks % 2 == 0:
      tabela = dbc.Card([
         dbc.CardHeader(html.H5("Tabela IPCA", className="text-center fw-bold")),
         dbc.CardBody(dbc.Table.from_dataframe(ipca_df, striped=True, bordered=True, hover=True, responsive=True))
      ], className="shadow-sm rounded-4")
      botao_texto = "Alternar para SINAPI"
   else:
      tabela = dbc.Card([
         dbc.CardHeader(html.H5("Tabela SINAPI", className="text-center fw-bold")),
         dbc.CardBody(dbc.Table.from_dataframe(sinapi_df, striped=True, bordered=True, hover=True, responsive=True))
      ], className="shadow-sm rounded-4")
      botao_texto = "Alternar para IPCA"

   return tabela, botao_texto
