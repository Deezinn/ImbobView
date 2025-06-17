import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import Input, Output, State, dcc, html

from components import nav
from db.datasets import ipca_df, sinapi_df
from app import app

PAGE_SIZE = 10

tabela = dbc.Container([

   html.H1("Visualização de Dados Econômicos", className="text-center my-4 fw-bold"),

   dbc.Row([
      dbc.Col([
         dbc.Button("Alternar para SINAPI", id="botao-alternar", color="primary", className="mb-4", style={'justify-content': 'center', 'align-items': 'center', 'text-align': 'center'}),
         html.Div(id="container-tabela", style={'justify-content': 'center', 'align-items': 'center', 'text-align': 'center'}),
         dbc.ButtonGroup([
             dbc.Button("Anterior", id="pagina-anterior", n_clicks=0, color="secondary"),
             dbc.Button("Próximo", id="pagina-proximo", n_clicks=0, color="secondary")
         ], className="mt-3 d-flex justify-content-center gap-2"),
         html.Div(id="pagina-atual", className="text-center mt-2")
      ], width=12),
   ], style={'justify-content': 'center', 'align-items': 'center', 'text-align': 'center'}),

], fluid=True, className="bg-light p-4")


@app.callback(
    Output("container-tabela", "children"),
    Output("botao-alternar", "children"),
    Output("pagina-atual", "children"),
    Input("botao-alternar", "n_clicks"),
    Input("pagina-anterior", "n_clicks"),
    Input("pagina-proximo", "n_clicks"),
    State("botao-alternar", "children"),
    State("pagina-atual", "children"),
)
def atualizar_tabela(n_clicks_alternar, n_clicks_anterior, n_clicks_proximo, botao_texto, pagina_texto):

    if n_clicks_alternar is None or n_clicks_alternar % 2 == 0:
        df = ipca_df
        botao_texto_novo = "Alternar para SINAPI"
        nome_tabela = "IPCA"
    else:
        df = sinapi_df
        botao_texto_novo = "Alternar para IPCA"
        nome_tabela = "SINAPI"


    if pagina_texto and pagina_texto.startswith("Página"):
        pagina_atual = int(pagina_texto.split()[-1])
    else:
        pagina_atual = 1


    max_paginas = (len(df) - 1) // PAGE_SIZE + 1


    ctx = dash.callback_context
    if not ctx.triggered:
        trigger_id = None
    else:
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if trigger_id == "pagina-anterior" and pagina_atual > 1:
        pagina_atual -= 1
    elif trigger_id == "pagina-proximo" and pagina_atual < max_paginas:
        pagina_atual += 1
    elif trigger_id == "botao-alternar":
        pagina_atual = 1
        
    start_idx = (pagina_atual - 1) * PAGE_SIZE
    end_idx = start_idx + PAGE_SIZE
    df_pagina = df.iloc[start_idx:end_idx]

    tabela = dbc.Card([
        dbc.CardHeader(html.H5(f"Tabela {nome_tabela} - Página {pagina_atual} de {max_paginas}", className="text-center fw-bold")),
        dbc.CardBody(dbc.Table.from_dataframe(df_pagina, striped=True, bordered=True, hover=True, responsive=True))
    ], className="shadow-sm rounded-4")

    pagina_display = f"Página {pagina_atual}"

    return tabela, botao_texto_novo, pagina_display
