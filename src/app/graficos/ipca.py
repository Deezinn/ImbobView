import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import Input, Output, dcc, html
import plotly.express as px

from components import nav
from db.datasets import ipca_df
from app import app

ipca_df['periodo'] = pd.to_datetime(ipca_df['periodo'])
ipca_df = ipca_df.sort_values('periodo')
ipca_df['periodo'] = pd.to_datetime(ipca_df['periodo']).dt.tz_localize(None)

grafico_layout = dbc.Container([

   html.H2("Visualização do IPCA", className="text-center my-4"),

   dbc.Row([
      dbc.Col([
         dbc.Label("Selecione o intervalo de datas:", style={'margin-right': '20px'}),
         dcc.DatePickerRange(
               id='filtro-data1',
               min_date_allowed=ipca_df['periodo'].min(),
               max_date_allowed=ipca_df['periodo'].max(),
               start_date=ipca_df['periodo'].min(),
               end_date=ipca_df['periodo'].max(),
               className="mb-3"
            ),
      ], md=6),

      dbc.Col([
         dbc.Label("Tipo de gráfico:", style={'margin-right': '20px'}),
         dbc.ButtonGroup([
               dbc.Button("Linha", id="btn-linha", color="primary"),
               dbc.Button("Barra", id="btn-barra", color="primary"),
               dbc.Button("Área", id="btn-area", color="primary"),
            ], className="mb-3", size="xl", style={'margin-top': '10px'}),
      ], md=6),
   ]),

   dbc.Row([
      dbc.Col([
         dbc.Card([
               dbc.CardHeader(html.H5("Gráfico IPCA", className="text-center fw-bold")),
               dbc.CardBody([
                  dcc.Graph(id='grafico-ipca', config={"displayModeBar": False})
               ])
            ], className="shadow-sm rounded-4 mb-4")
      ], md=6),

      dbc.Col([
         dbc.Card([
               dbc.CardHeader(html.H5("IPCA Acumulado no Período", className="text-center fw-bold")),
               dbc.CardBody([
                  dcc.Graph(id='grafico-acumulado', config={"displayModeBar": False})
               ])
            ], className="shadow-sm rounded-4 mb-4")
      ], md=6),
   ]),

   dbc.Row([
      dbc.Col([
         dbc.Card([
               dbc.CardHeader(html.H5("Variação Percentual Mensal", className="text-center fw-bold")),
               dbc.CardBody([
                  dcc.Graph(id='grafico-var-percentual', config={"displayModeBar": False})
               ])
            ], className="shadow-sm rounded-4 mb-4")
      ], md=6),

      dbc.Col([
         dbc.Card([
               dbc.CardHeader(html.H5("Média Móvel 3 Meses", className="text-center fw-bold")),
               dbc.CardBody([
                  dcc.Graph(id='grafico-media-movel', config={"displayModeBar": False})
               ])
            ], className="shadow-sm rounded-4 mb-4")
      ], md=6),
   ]),

], fluid=True, className="bg-light p-4")


@app.callback(
   Output("grafico-ipca", "figure"),
   Output("grafico-acumulado", "figure"),
   Output("grafico-var-percentual", "figure"),
   Output("grafico-media-movel", "figure"),
   Output("btn-linha", "color"),
   Output("btn-barra", "color"),
   Output("btn-area", "color"),
   Input("filtro-data1", "start_date"),
   Input("filtro-data1", "end_date"),
   Input("btn-linha", "n_clicks"),
   Input("btn-barra", "n_clicks"),
   Input("btn-area", "n_clicks"),
)
def atualizar_graficos(start_date, end_date, n_linha, n_barra, n_area):

   df = ipca_df[(ipca_df['periodo'] >= pd.to_datetime(start_date)) & (ipca_df['periodo'] <= pd.to_datetime(end_date))].copy()

   ctx = dash.callback_context
   tipo = 'linha'

   if ctx.triggered:
      botao_id = ctx.triggered[0]['prop_id'].split('.')[0]
      if botao_id == 'btn-barra':
         tipo = 'barra'
      elif botao_id == 'btn-area':
         tipo = 'area'

   if tipo == 'linha':
      fig_ipca = px.line(df, x='periodo', y='valor', markers=True, title='IPCA - Linha')
   elif tipo == 'barra':
      fig_ipca = px.bar(df, x='periodo', y='valor', title='IPCA - Barras')
   else:
      fig_ipca = px.area(df, x='periodo', y='valor', title='IPCA - Área')

   df['acumulado'] = df['valor'].cumsum()
   if tipo == 'linha':
      fig_acum = px.line(df, x='periodo', y='acumulado', markers=True, title='IPCA Acumulado')
   elif tipo == 'barra':
      fig_acum = px.bar(df, x='periodo', y='acumulado', title='IPCA Acumulado')
   else:
      fig_acum = px.area(df, x='periodo', y='acumulado', title='IPCA Acumulado')

   df['var_percentual'] = df['valor'].pct_change() * 100
   df = df.dropna()
   if tipo == 'linha':
      fig_var = px.line(df, x='periodo', y='var_percentual', markers=True, title='Variação Percentual Mensal (%)')
   elif tipo == 'barra':
      fig_var = px.bar(df, x='periodo', y='var_percentual', title='Variação Percentual Mensal (%)')
   else:
      fig_var = px.area(df, x='periodo', y='var_percentual', title='Variação Percentual Mensal (%)')

   df['media_movel_3m'] = df['valor'].rolling(window=3).mean()
   df = df.dropna(subset=['media_movel_3m'])
   if tipo == 'linha':
      fig_mm = px.line(df, x='periodo', y='media_movel_3m', markers=True, title='Média Móvel 3 Meses')
   elif tipo == 'barra':
      fig_mm = px.bar(df, x='periodo', y='media_movel_3m', title='Média Móvel 3 Meses')
   else:
      fig_mm = px.area(df, x='periodo', y='media_movel_3m', title='Média Móvel 3 Meses')

   for fig in [fig_ipca, fig_acum, fig_var, fig_mm]:
      fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), template='plotly_white', height=400)

   cor_linha = "primary" if tipo == 'linha' else "secondary"
   cor_barra = "primary" if tipo == 'barra' else "secondary"
   cor_area = "primary" if tipo == 'area' else "secondary"

   return fig_ipca, fig_acum, fig_var, fig_mm, cor_linha, cor_barra, cor_area
