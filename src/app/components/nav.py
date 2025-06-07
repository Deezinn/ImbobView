import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from app import app  # Importa a instância do app

LOGO = "assets/img/mao.png"

navbar = dbc.Navbar(
   dbc.Container(
      [
         html.A(
               dbc.Row(
                  [
                     dbc.Col(dbc.NavbarBrand("ImobView", className="text-white ")),
                     dbc.Col(html.Img(src=LOGO, height="30px", style={'margin-left': '-20px'})),
                  ],
                  align="center",
                  className="g-0",
               ),
               href="https://unsplash.com/s/photos/imobiliario",
               style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
               dbc.Row(
                  [
                  dbc.Col(
                        dbc.Nav(
                              [
                                 dbc.NavItem(dbc.NavLink('Home', href='/', className='text-white')),
                                 dbc.NavItem(dbc.NavLink('Página 1', href='/pagina1', className='text-white')),
                                 dbc.NavItem(dbc.NavLink('Página 2', href='/pagina2', className='text-white')),
                              ],
                              className="justify-content-center",
                              navbar=True,
                           ),
                           width="auto"
                     )
                  ],
                  className="w-100 justify-content-center",
               ),
               id="navbar-collapse",
               is_open=False,
               navbar=True,
            ),
      ]
   ),
   color="black",
   dark=True,
   expand="md",
   className="w-100",
)
