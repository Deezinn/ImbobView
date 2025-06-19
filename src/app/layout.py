import dash
import dash_bootstrap_components as dbc
import pandas as pd
from components.header import header
from dash import Input, Output, State, dcc, html
# import pages
from home.page import home
from tabelas.page import tabela
from graficos.ipca import grafico_layout
from graficos.sinapi import ipca_layout
from sobre.page import about_page
# import from folders
from app import app

# =========  Layout  =========== #
app.layout = dbc.Container(children=[
   dcc.Location(id="url"),
   dbc.Row([
      header,
   ]),
   dbc.Row([
         html.Img(src='assets/img/sinal-de-seta-para-baixo-para-navegar.png', style={'width': '50px','margin-top': '10px'}, className='bouncing-arrow'),
         dbc.Container(id="page-content", fluid=True, style={'margin-top': '10px'}),
         html.Div('© 2025 Imbob - Todos os direitos reservados.',style={'textAlign': 'center','padding': '10px','backgroundColor': "#000000",'left': '0','bottom': '0','width': '100%','fontSize': '14px','color': 'WHITE'}
)
   ], style={'display': 'flex', 'justify-content': 'center'})
], fluid=True)


# ======= Callbacks ======== #
# URL callback to update page content
@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def render_page_content(pathname):
   if pathname == '/home' or pathname == '/':
      return home
   elif pathname == '/tabelas':
      return tabela
   elif pathname == '/ipca':
      return grafico_layout
   elif pathname == '/sinapi':
      return ipca_layout
   elif pathname == '/sobre':
      return about_page
   return dbc.Container([
         html.H1("404: Not found", className="text-danger"),
         html.Hr(),
         html.P(f"O caminho '{pathname}' não foi reconhecido..."),
         html.P("Use a NavBar para retornar ao sistema de maneira correta.")
      ])

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8050)
