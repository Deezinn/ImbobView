

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html

import pandas as pd

from components import nav

from app import app


home = dbc.Container(children=[
   html.H1("Aqui esta vazio")
], fluid=True, style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'text-align': 'center','height': '500px' ,'with': '100vh'})
