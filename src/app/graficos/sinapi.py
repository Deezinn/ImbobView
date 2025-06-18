import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html
from db.datasets import sinapi_df

from app import app

# Pré-processamento
sinapi_df['periodo'] = pd.to_datetime(sinapi_df['periodo'])
sinapi_df = sinapi_df.sort_values('periodo')
sinapi_df['periodo'] = pd.to_datetime(sinapi_df['periodo']).dt.tz_localize(None)
df = sinapi_df.copy()

# Opções para filtros
ufs_options = [{'label': uf, 'value': uf} for uf in df['unidade_da_federacao'].unique()]
tipo_proj_options = [{'label': tp, 'value': tp} for tp in sorted(df['tipo_de_projeto'].unique())]
padrao_acab_options = [{'label': pa, 'value': pa} for pa in sorted(df['padrao_de_acabamento'].unique())]

# Layout
ipca_layout = html.Div([
   html.H1("Análise de Dados SINAPI", style={
      "textAlign": "center", "marginBottom": "30px", "fontFamily": "Arial", "color": "#000000"
   }),

   html.Div([
      html.Div([
         html.Label("Unidades da Federação", style={"fontWeight": "bold"}),
         dcc.Dropdown(
            options=ufs_options,
            id='uf-filter',
            multi=True,
            placeholder="Ex: Pernambuco, Bahia...",
            value=['Pernambuco']
         ),
      ], style={"flex": "1"}),

      html.Div([
         html.Label("Tipo de Projeto", style={"fontWeight": "bold"}),
         dcc.Dropdown(
            options=tipo_proj_options,
            id='tipo-filter',
            multi=True,
            placeholder="Ex: Edificação, Instalação...",
            value=[' Casa popular, 1 pavimento, sala, 2 quartos, circulação, banheiro e cozinha']
         ),
      ], style={"flex": "1"}),

      html.Div([
         html.Label("Padrão de Acabamento", style={"fontWeight": "bold"}),
         dcc.Dropdown(
            options=padrao_acab_options,
            id='padrao-filter',
            multi=True,
            placeholder="Ex: Baixo, Normal, Alto"
         ),
      ], style={"flex": "1"}),

      html.Div([
         html.Label("Período", style={"fontWeight": "bold"}),
         dcc.DatePickerRange(
            id='data-filter',
            start_date=df['periodo'].min(),
            end_date=df['periodo'].max(),
            display_format='MMMM Y',
            style={"width": "100%"}
         ),
      ], style={"flex": "1"})
   ], style={
      "display": "flex", "gap": "20px", "flexWrap": "wrap",
      "marginBottom": "40px", "padding": "10px 20px"
   }),

   html.Div([
      dcc.Graph(id='linha-temporal'),
      dcc.Graph(id='boxplot-uf'),
      dcc.Graph(id='barras-agrupadas'),
      dcc.Graph(id='sunburst')
   ], style={"padding": "0 20px"})
], style={
   "backgroundColor": "#F9FAFB", "padding": "40px", "minHeight": "100vh",
   "fontFamily": "Arial, sans-serif"
})

@app.callback(
   Output('linha-temporal', 'figure'),
   Output('boxplot-uf', 'figure'),
   Output('barras-agrupadas', 'figure'),
   Output('sunburst', 'figure'),
   Input('uf-filter', 'value'),
   Input('tipo-filter', 'value'),
   Input('padrao-filter', 'value'),
   Input('data-filter', 'start_date'),
   Input('data-filter', 'end_date'),
)
def update_graphs(ufs, tipos, padroes, data_inicio, data_fim):
   dff = df.copy()
   if isinstance(ufs, str):
      ufs = [ufs]
   if isinstance(tipos, str):
      tipos = [tipos]
   if isinstance(padroes, str):
      padroes = [padroes]

   if ufs:
      dff = dff[dff['unidade_da_federacao'].isin(ufs)]
   if tipos:
      dff = dff[dff['tipo_de_projeto'].isin(tipos)]
   if padroes:
      dff = dff[dff['padrao_de_acabamento'].isin(padroes)]
   dff = dff[(dff['periodo'] >= data_inicio) & (dff['periodo'] <= data_fim)]

   # Gráfico de linha ou aviso
   if dff.empty:
      linha = px.line(title="Sem dados para exibir")
      linha.update_layout(
         xaxis={'visible': False},
         yaxis={'visible': False},
         annotations=[{
            'text': "Sem dados disponíveis para os filtros selecionados.",
            'xref': 'paper',
            'yref': 'paper',
            'showarrow': False,
            'font': {'size': 16}
         }]
      )
      return linha, linha, linha, linha, linha

   # Linha temporal
   df_agg = dff.groupby(['periodo']).valor.mean().reset_index()
   linha = px.area(
      df_agg,
      x='periodo',
      y='valor',
      title="Evolução do Valor Médio (Área Acumulada)",
      template="plotly_white"
   )
   linha.update_traces(mode='lines', line=dict(width=2), fill='tozeroy')
   linha.update_layout(
      xaxis_title="Período",
      yaxis_title="Valor Médio",
      hovermode="x unified",
      margin=dict(l=40, r=40, t=60, b=40)
   )

   # Boxplot por UF
   box = px.box(
      dff, x='unidade_da_federacao', y='valor',
      title="Distribuição de Valor por UF",
      template="plotly_white"
   )

   # Barras agrupadas
   barras = px.bar(
      dff.groupby(['unidade_da_federacao', 'padrao_de_acabamento']).valor.mean().reset_index(),
      x='unidade_da_federacao', y='valor', color='padrao_de_acabamento', barmode='group',
      title="Valor Médio por UF e Padrão de Acabamento",
      template="plotly_white"
   )

   # Sunburst
   sunburst = px.sunburst(
      dff, path=['tipo_de_projeto', 'padrao_de_acabamento', 'unidade_da_federacao'],
      values='valor',
      title="Hierarquia por Tipo > Padrão > UF",
      template="plotly_white"
   )

   return linha, box, barras, sunburst

