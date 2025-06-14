import dash
import dash_bootstrap_components as dbc
from dash import html
from dash_iconify import DashIconify

home = dbc.Container(fluid=True, style={'padding': '40px', 'height': '80vh'}, children=[

   dbc.Row([
      dbc.Col([
         html.H1("Este projeto", className="mb-4", style={'display': 'flex','justifyContent': 'center', 'text-align': 'center', 'align-items':'center'}
         ),
         html.H4(
               "O projeto de dados imobiliários tem como objetivo informar e divulgar, "
               "de forma visual e intuitiva, indicadores relevantes para o mercado habitacional brasileiro.",
               className="mb-5",
               style={"fontSize": "18px", 'display': 'flex','justifyContent': 'center', 'text-align': 'center', 'align-items':'center'}
            ),

            html.H2("Dados coletados", className="mb-4",style={'display': 'flex', 'justify-content': 'center', 'margin-top': '100px'})
      ])
   ], ),

   dbc.Row([
      dbc.Col([
         dbc.Card([
               dbc.CardBody([
                  html.Div([
                     DashIconify(icon="mdi:hammer-wrench", width=24, className="me-2"),
                     html.B("SINAPI"),
                     html.Span(" — Sistema Nacional de Pesquisa de Custos e Índices da Construção Civil.")
                  ], className="d-flex align-items-center")
               ])
            ], color="light", className="mb-3"),

            dbc.Card([
               dbc.CardBody([
                  html.Div([
                     DashIconify(icon="mdi:home-city-outline", width=24, className="me-2"),
                     html.B("FIPEZAP"),
                     html.Span(" — Índice de Preços de Imóveis Residenciais e Comerciais com abrangência nacional.")
                  ], className="d-flex align-items-center")
               ])
            ], color="light", className="mb-3"),

            dbc.Card([
               dbc.CardBody([
                  html.Div([
                     DashIconify(icon="mdi:cash-multiple", width=24, className="me-2"),
                     html.B("SELIC"),
                     html.Span(" — Taxa básica de juros da economia.")
                  ], className="d-flex align-items-center")
               ])
            ], color="light", className="mb-3"),

            dbc.Card([
               dbc.CardBody([
                  html.Div([
                     DashIconify(icon="mdi:home-heart", width=24, className="me-2"),
                     html.B("MCMV"),
                     html.Span(" — Programa Minha Casa, Minha Vida.")
                  ], className="d-flex align-items-center")
               ])
            ], color="light", className="mb-3"),
      ], lg=6, md=10)
   ],style={'display': 'flex', 'justify-content': 'center'})
])
