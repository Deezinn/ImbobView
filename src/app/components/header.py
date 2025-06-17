import dash_bootstrap_components as dbc
from components.nav import navbar
from dash import Input, Output, State, dcc, html

from app import app

header = dbc.Container([
   # Linha da navbar
   dbc.Row([
      dbc.Col(navbar)
   ]),

   # Linha com imagem + texto e botões ao lado
   dbc.Row([
      # Coluna da imagem + título
      dbc.Col([
         html.Div([
            html.Div([
               html.Img(
                  id='Ia-image',
                  src='/assets/img/inteligencia-artificial.png',
                  style={'margin-left': '80px','margin-right': '10px', 'width': '80px'}
               )
            ]),

            html.Div([
               html.H3(id='title-bot', children='Olá, usuário!', className='text-white'),
               html.H5(id='descrie-bot', children='Conheça nossa plataforma sobre dados Imobiliários', className='text-white')
            ], style={'margin-left': '20px'})
         ],
         style={
            'display': 'flex',
            'flexDirection': 'row',
            'alignItems': 'center',
            'margin-top': '40px'
         })
      ], md=8),

      # Coluna dos botões
      dbc.Col([
         dbc.Row([
            dbc.Col([
               dbc.Button("Informações", className="custom-button me-3", style={'width': '100%'}),
               dbc.Button("Conheça nossa IA", className="custom-button2", style={'width': '100%'})
            ], className="d-grid gap-3 d-md-flex justify-content-md-center")
         ], className="mt-5 me-5")
      ], md=4,),
   ],style={'padding': '10px' ,'margin-right': '10px'}),

   # Linha da linha horizontal centralizada
   dbc.Row([
      dbc.Col([
         html.Hr(style={
            'backgroundColor': 'white',
            'height': '3px',
            'border': 'none',
            'marginTop': '80px',
            'marginBottom': '20px',
            'width': '86%',
            'marginLeft': 'auto',
            'marginRight': 'auto',
         })
      ])
   ]),

   # Linha do card e título
   dbc.Row([
      dbc.Col([
         dbc.Row([

            # Card 1 - IPCA variação
            dbc.Col([
               dbc.Card(
                  [
                     dbc.CardHeader([
                        dbc.Row([
                           dbc.Col([
                              html.Img(src='https://cdn-icons-png.flaticon.com/128/1006/1006553.png',
                                       style={'width': '40px', 'margin': '10px'})  # ícone de gráfico de linha
                           ]),
                           dbc.Col([
                              html.P('-0.45%', style={
                                 'display': 'flex',
                                 'justify-content': 'end',
                                 'margin-top': '20px',
                                 'margin-right': '20px',
                                 'color': '#E74C3C'  # vermelho para queda
                              })
                           ])
                        ])
                     ]),
                     dbc.CardFooter([
                        dbc.Row([
                           dbc.Col([
                              html.H1('0,12%', style={'color': 'white'})
                           ]),
                           dbc.Col([
                              html.H3('IPCA', style={'color': 'white'})
                           ])
                        ])
                     ], className="d-md-flex justify-content-center text-center mt-5"),
                  ],
                  style={
                     "width": "24rem",
                     "height": "250px",
                     "background-color": '#111111',
                     'border-radius': '2px',
                     'margin-top': '5px'
                  },
               )
            ]),

            # Card 2 - IPCA acumulado
            dbc.Col([
               dbc.Card(
                  [
                     dbc.CardHeader([
                        dbc.Row([
                           dbc.Col([
                              html.Img(src='https://cdn-icons-png.flaticon.com/128/1006/1006553.png',
                                       style={'width': '40px', 'margin': '10px'})
                           ]),
                           dbc.Col([
                              html.P('+1.10%', style={
                                 'display': 'flex',
                                 'justify-content': 'end',
                                 'margin-top': '20px',
                                 'margin-right': '20px',
                                 'color': '#4CAF50'  # verde para alta
                              })
                           ])
                        ])
                     ]),
                     dbc.CardFooter([
                        dbc.Row([
                           dbc.Col([
                              html.H1('4,65%', style={'color': 'white'})
                           ]),
                           dbc.Col([
                              html.H3('IPCA Acumulado', style={'color': 'white'})
                           ])
                        ])
                     ], className="d-md-flex justify-content-center mt-5"),
                  ],
                  style={
                     "width": "24rem",
                     "height": "250px",
                     "background-color": '#111111',
                     'border-radius': '2px',
                     'margin-top': '5px'
                  },
               )
            ]),

            # Card 3 - SINAPI valor
            dbc.Col([
               dbc.Card(
                  [
                     dbc.CardHeader([
                        dbc.Row([
                           dbc.Col([
                              html.Img(src='https://cdn-icons-png.flaticon.com/128/685/685655.png',
                                       style={'width': '40px', 'margin': '10px'})  # ícone de construção
                           ]),
                           dbc.Col([
                              html.P('+0.8%', style={
                                 'display': 'flex',
                                 'justify-content': 'end',
                                 'margin-top': '20px',
                                 'margin-right': '20px',
                                 'color': '#4CAF50'  # verde para alta
                              })
                           ])
                        ])
                     ]),
                     dbc.CardFooter([
                        dbc.Row([
                           dbc.Col([
                              html.H1('1.092,32', style={'color': 'white'})
                           ]),
                           dbc.Col([
                              html.H3('SINAPI', style={'color': 'white'})
                           ])
                        ])
                     ], className="d-md-flex justify-content-center mt-5"),
                  ],
                  style={
                     "width": "24rem",
                     "height": "250px",
                     "background-color": '#111111',
                     'border-radius': '2px',
                     'margin-top': '5px'
                  },
               )
            ]),

            # Card 4 - SINAPI variação mensal
            dbc.Col([
               dbc.Card(
                  [
                     dbc.CardHeader([
                        dbc.Row([
                           dbc.Col([
                              html.Img(src='https://cdn-icons-png.flaticon.com/128/685/685655.png',
                                       style={'width': '40px', 'margin': '10px'})
                           ]),
                           dbc.Col([
                              html.P('-0.3%', style={
                                 'display': 'flex',
                                 'justify-content': 'end',
                                 'margin-top': '20px',
                                 'margin-right': '20px',
                                 'color': '#E74C3C'  # vermelho para queda
                              })
                           ])
                        ])
                     ]),
                     dbc.CardFooter([
                        dbc.Row([
                           dbc.Col([
                              html.H1('1.080,00', style={'color': 'white'})
                           ]),
                           dbc.Col([
                              html.H3('SINAPI Mês', style={'color': 'white'})
                           ])
                        ])
                     ], className="d-md-flex justify-content-center mt-5"),
                  ],
                  style={
                     "width": "24rem",
                     "height": "250px",
                     "background-color": '#111111',
                     'border-radius': '2px',
                     'margin-top': '5px'
                  },
               )
            ]),
         ])
      ], className="d-md-flex justify-content-start", style={'marginLeft': '30px', 'margin-bottom': '30px', 'padding': '20px'}),
   ],style={'padding': '70px'}),

], fluid=True, style={'height': '100%','background': 'black', 'padding': '20px'})
