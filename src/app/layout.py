import dash
import dash_bootstrap_components as dbc
import pandas as pd
from components.header import header
from dash import Input, Output, State, dcc, html
# import pages
from home.page import home
from tabelas.page import tabela
# import from folders
from app import app

# =========  Layout  =========== #
app.layout = dbc.Container(children=[
   dcc.Location(id="url"),
   dbc.Row([
      header,
   ]),
   dbc.Row([
         html.Img(src='assets/img/sinal-de-seta-para-baixo-para-navegar.png', style={'width': '50px','margin-top': '20px'}),
         dbc.Container(id="page-content", fluid=True, )
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
   return dbc.Container([
         html.H1("404: Not found", className="text-danger"),
         html.Hr(),
         html.P(f"O caminho '{pathname}' não foi reconhecido..."),
         html.P("Use a NavBar para retornar ao sistema de maneira correta.")
      ])

if __name__ == '__main__':
   app.run(debug=True)


#
