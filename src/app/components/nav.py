import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from app import app  

LOGO = "assets/img/mao.png"

navbar = dbc.Navbar(
   dbc.Container(
      [
         html.A(
               dbc.Row(
                  [
                     dbc.Col(dbc.NavbarBrand("ImobView", className="text-white ")),
                     dbc.Col(html.Img(src=LOGO, height="30px", style={'margin-left': '-10px'})),
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
                                 dbc.NavItem(dbc.NavLink("Home", href="/", id="nav-home")),
                                 dbc.NavItem(dbc.NavLink("IPCA", href="/ipca", id="nav-ipca")),
                                 dbc.NavItem(dbc.NavLink("SINAPI", href="/sinapi", id="nav-sinapi")),
                                 dbc.NavItem(dbc.NavLink("Tabelas", href="/tabelas", id="nav-tabelas")),
                                 dbc.NavItem(dbc.NavLink("Sobre", href="/sobre", id="nav-sobre")),
                              ],
                              className="justify-content-center mt-2",
                              navbar=True,
                           ),
                           width="auto"
                     ),
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
   expand="sm",
   className="w-100",
)

@app.callback(
   Output("nav-home", "className"),
   Output("nav-ipca", "className"),
   Output("nav-tabelas", "className"),
   Output("nav-sinapi", "className"),
   Output("nav-sobre", "className"),
   Input("url", "pathname")
)
def update_active_class(pathname):
   def nav_class(link_path):
      return "text-black nav-link-custom bg-white rounded-1" if pathname == link_path else "nav-link-custom rounded-1"

   return (
      nav_class("/"),
      nav_class("/ipca"),
      nav_class("/tabelas"),
      nav_class("/sinapi"),
      nav_class("/sobre")
   )

@app.callback(
   Output("navbar-collapse", "is_open"),
   [Input("navbar-toggler", "n_clicks")],
   [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
   if n:
      return not is_open
   return is_open
