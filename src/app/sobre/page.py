import dash_bootstrap_components as dbc
from dash import html

about_page = dbc.Container(
    [
        dbc.Row(
            html.H1("Sobre os Desenvolvedores", className="text-center text-black mb-5"),
            justify="center",
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            html.Div(
                                html.Img(
                                    src="/assets/img/andre.jpeg",
                                    alt="Desenvolvedor 1",
                                    style={
                                        "width": "180px",
                                        "height": "180px",
                                        "objectFit": "cover",
                                        "borderRadius": "50%",
                                        "border": "3px solid #4CAF50",
                                        "margin": "auto",
                                        "display": "block",
                                    },
                                ),
                                className="mb-3",
                            ),

                            dbc.CardBody(
                                html.P(
                                    "André Luiz: Responsável pelo Front-end e pipeline.",
                                    className="text-center text-black",
                                )
                            ),
                        ],
                        style={"backgroundColor": "#FFFFFF", "borderRadius": "10px"},
                        className="p-3",
                    ),
                    width=4,
                    className="mx-auto",
                ),
                dbc.Col(width=1),

                dbc.Col(
                    dbc.Card(
                        [
                            html.Div(
                                html.Img(
                                    src="/assets/img/antonio.jpeg",
                                    alt="Antonio Lemos",
                                    style={
                                        "width": "180px",
                                        "height": "180px",
                                        "objectFit": "cover",
                                        "borderRadius": "50%",
                                        "border": "3px solid #2196F3",
                                        "margin": "auto",
                                        "display": "block",
                                    },
                                ),
                                className="mb-3",
                            ),

                            dbc.CardBody(
                                html.P(
                                    "Antonio Lemos: Responsavel pela infraestrutura (dvops)",
                                    className="text-center text-black",
                                )
                            ),
                        ],
                        style={"backgroundColor": "#FFFFFF", "borderRadius": "10px"},
                        className="p-3",
                    ),
                    width=4,
                    className="mx-auto",
                ),
            ],
            justify="center",
            className="mb-5",
            style={'margin-top': '50px'}
        ),
    ],
    fluid=True,
    style={"backgroundColor": "white", "minHeight": "70vh", "padding": "50px"},
)
