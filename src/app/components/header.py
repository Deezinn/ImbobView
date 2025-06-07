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
                  style={'margin': '40px', 'width': '80px'}
               )
            ]),

            html.Div([
               html.H3(id='title-bot', children='Olá, usuário!', className='text-white'),
               html.H5(id='descrie-bot', children='Conheça nossa plataforma de dados sobre dados Imobiliários', className='text-white')
            ])
         ],
         style={
            'display': 'flex',
            'flexDirection': 'row',
            'alignItems': 'center',
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
   ],style={'padding': '10px'}),

   # Linha da linha horizontal centralizada
   dbc.Row([
      dbc.Col([
         html.Hr(style={
            'backgroundColor': 'white',
            'height': '3px',
            'border': 'none',
            'marginTop': '20px',
            'marginBottom': '20px',
            'width': '90%',
            'marginLeft': 'auto',
            'marginRight': 'auto',
         })
      ])
   ]),

   # Linha do card e título
   dbc.Row([
      dbc.Col([
         dbc.Row([
            html.H1('Dados recentes -', className='text-white', style={'margin-bottom':'30px',}),
            dbc.Col([
               dbc.Row([
                  dbc.Col([
                     dbc.Card(
                        [
                           dbc.CardHeader([
                              dbc.Row([
                                 dbc.Col([
                                    html.Img(src='https://cdn-icons-png.flaticon.com/128/9428/9428429.png', style={'width': '40px', 'margin': '10px'})
                                 ]),
                                 dbc.Col([
                                    html.P('-20%', style={'display': 'flex', 'justify-content': 'end', 'margin-top': '20px', 'margin-right': '20px', 'color': 'white'})
                                 ])
                              ])
                              ]),
                           dbc.CardFooter([
                              dbc.Row([
                                 dbc.Col([
                                    html.H1('1,092.32', style={'color': 'white'})
                                 ]),
                                 dbc.Col([
                                    html.H3('$', style={'color': 'white'})
                                 ])
                              ])
                              ], className="d-md-flex justify-content-center text-center mt-5"),
                        ],
                        style={
                           "width": "24rem",  # Aumente aqui a largura do card
                           "height": "250px",  # Aumente aqui a altura do card
                           "background-color": '#111111',
                           'border-radius': '2px'
                        },
                     )
                  ]),
                  dbc.Col([
                     dbc.Card(
                        [
                           dbc.CardHeader([
                              dbc.Row([
                                 dbc.Col([
                                    html.Img(src='https://cdn-icons-png.flaticon.com/128/9428/9428429.png', style={'width': '40px', 'margin': '10px'})
                                 ]),
                                 dbc.Col([
                                    html.P('-20%', style={'display': 'flex', 'justify-content': 'end', 'margin-top': '20px', 'margin-right': '20px', 'color': 'white'})
                                 ])
                              ])
                              ]),
                           dbc.CardFooter([
                              dbc.Row([
                                 dbc.Col([
                                    html.H1('1,092.32', style={'color': 'white'})
                                 ]),
                                 dbc.Col([
                                    html.H3('$', style={'color': 'white'})
                                 ])
                              ])
                              ], className="d-md-flex justify-content-center mt-5"),
                        ],
                        style={
                           "width": "24rem",  # Aumente aqui a largura do card
                           "height": "250px",  # Aumente aqui a altura do card
                           "background-color": '#111111',
                           'border-radius': '2px'
                        },
                     )
                  ]),
                  dbc.Col([
                     dbc.Card(
                        [
                           dbc.CardHeader([
                              dbc.Row([
                                 dbc.Col([
                                    html.Img(src='https://cdn-icons-png.flaticon.com/128/9428/9428429.png', style={'width': '40px', 'margin': '10px'})
                                 ]),
                                 dbc.Col([
                                    html.P('-20%', style={'display': 'flex', 'justify-content': 'end', 'margin-top': '20px', 'margin-right': '20px', 'color': 'white'})
                                 ])
                              ])
                              ]),
                           dbc.CardFooter([
                              dbc.Row([
                                 dbc.Col([
                                    html.H1('1,092.32', style={'color': 'white'})
                                 ]),
                                 dbc.Col([
                                    html.H3('$', style={'color': 'white'})
                                 ])
                              ])
                              ], className="d-md-flex justify-content-center mt-5"),
                        ],
                        style={
                           "width": "24rem",  # Aumente aqui a largura do card
                           "height": "250px",  # Aumente aqui a altura do card
                           "background-color": '#111111',
                           'border-radius': '2px'
                        },
                     )
                  ]),
                  dbc.Col([
                     dbc.Card(
                        [
                           dbc.CardHeader([
                              dbc.Row([
                                 dbc.Col([
                                    html.Img(src='https://cdn-icons-png.flaticon.com/128/9428/9428429.png', style={'width': '40px', 'margin': '10px'})
                                 ]),
                                 dbc.Col([
                                    html.P('-20%', style={'display': 'flex', 'justify-content': 'end', 'margin-top': '20px', 'margin-right': '20px', 'color': 'white'})
                                 ])
                              ])
                              ]),
                           dbc.CardFooter([
                              dbc.Row([
                                 dbc.Col([
                                    html.H1('1,092.32', style={'color': 'white'})
                                 ]),
                                 dbc.Col([
                                    html.H3('$', style={'color': 'white'})
                                 ])
                              ])
                              ], className="d-md-flex justify-content-center mt-5"),
                        ],
                        style={
                           "width": "24rem",  # Aumente aqui a largura do card
                           "height": "250px",  # Aumente aqui a altura do card
                           "background-color": '#111111',
                           'border-radius': '2px'
                        },
                     )
                  ]),
               ])
            ])
         ])
      ], className="d-md-flex justify-content-start", style={'marginLeft': '30px', 'margin-bottom': '30px', 'padding': '20px'}),
   ])

], fluid=True, style={'height': '100%', 'background-color': 'black', 'padding': '20px'})
