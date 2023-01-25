from dash import Dash, html, Input, Output, State, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

app = Dash(__name__, title = 'PlatziConf Hawaii',
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

LOGO = "assets\images\platzi-logo.png"

app.layout = dbc.Container([

    ############################################### header ###############################################

    html.Nav([
        dbc.Navbar(
            dbc.Container(
                [
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src=LOGO, height="30px")),
                                dbc.Col(dbc.NavbarBrand("Conf Hawaii", className="ms-2")),
                            ],
                            align="center",
                            className="g-0",
                        ),
                        href="https://google.com",
                        style={"textDecoration": "none"},
                    ),
                    dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                    dbc.Collapse([

                        dbc.Row([dbc.Col(children=[dbc.NavItem(dbc.NavLink("Conferencia", href="#"))])],
                                    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0", align="center"),

                        dbc.Row([dbc.Col(children=[dbc.NavItem(dbc.NavLink("Oradores", href="#"))])],
                                    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0", align="center"),

                        dbc.Row([dbc.Col(children=[dbc.NavItem(dbc.NavLink("Lugar y fecha", href="#"))])],
                                    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0", align="center"),

                        dbc.Row([dbc.Col(children=[dbc.NavItem(dbc.NavLink("Conviertete en orador", href="#"))])],
                                    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0", align="center"),

                        dbc.Row([dbc.Col(children=[dbc.NavItem(dbc.NavLink("Tickets", href="#"))])],
                                    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0", align="center"),

                    ], id="navbar-collapse", is_open=False, navbar=True,
                    ),
                ]
            ),
            color="dark",
            dark=True,
        ), 

    ]),


    ################################################ Main ################################################
    
    
    dbc.Container([

        dbc.Carousel(
            items=[
                {"key": "1", "src": "/assets/images/hawaii.jpg"},
                {"key": "2", "src": "/assets/images/hawaii2.jpg"},
                {"key": "3", "src": "assets/images/hawaii3.jpeg"},
            ],
            controls=False,
            indicators=False,
            interval=2000,
            ride="carousel",      
        ),

        dbc.Container([
            dbc.Container([
                dbc.Row(children=[

                    dbc.Col([

                    html.H1("Platzi conf Hawaii", className="sub_title"),
                    html.P("Lorem ipsum dolor sit amet consectetur, adipisicing elit. Adipisci, illo eos ad \
                            inventore reiciendis alias impedit repellendus dolorum. Itaque cum perspiciatis nihil \
                            magni, voluptatem quibusdam asperiores aperiam animi ipsa iure! Tenetur eligendi \
                            blanditiis soluta necessitatibus consectetur sit laudantium ipsum iste explicabo \
                            architecto velit vel aperiam nesciunt ut asperiores commodi dignissimos delectus \
                            mollitia adipisci est reprehenderit a, autem placeat qui. Fugit?"),
                    dbc.Button("Quiero ser orador", outline=True, color="dark", className="me-1"),
                    dbc.Button("Comprar tickets", className="btn-platzi"), 

                    ],width={"size": 6, "offset": 6}),

                ], className="row text-center"), 
            ]),
        ], id="overlay"),


    ], fluid=True, id="main", className='main'),



    ############################################## Speakers ##############################################

    html.Div(id='speakers', className="mt-4", children=[
        dbc.Container([

            dbc.Row(className="col text-center", children=[
                dbc.Col([
                    html.Small("Conoce a los"),
                    html.H2("Oradores"),
                ]),
            ]),

            dbc.Row(children=[

                dbc.Col(className="col-12 col-md-6 col-lg-4 mb-4", children=[

                    dbc.Card([
                            dbc.CardImg(src="assets/speakers/buoh.jpg", top=True),
                            dbc.CardBody([
                                html.Div(className="badges", children=[
                                    html.Span([
                                        dbc.Badge("JavaScript", color="warning", className="me-1"),
                                        dbc.Badge("Spark", color="success", className="me-1"),
                                    ]),
                                ]),
                                html.H5("Orador 1"),
                                html.P("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora \
                                        voluptatem quasi doloremque rerum, nulla voluptate. Accusamus, tempora. \
                                        Consectetur tempora fuga quasi, cumque atque obcaecati quisquam dolorem \
                                        iste voluptatum dolorum nostrum.", className="card-text"),
                            ]),
                        ],
                    )
                ]),


                dbc.Col(className="col-12 col-md-6 col-lg-4 mb-4", children=[

                    dbc.Card([
                            dbc.CardImg(src="assets/speakers/leon.jpg", top=True),
                            dbc.CardBody([
                                html.Div(className="badges", children=[
                                    html.Span([
                                        dbc.Badge("JavaScript", color="warning", className="me-1"),
                                        dbc.Badge("Spark", color="success", className="me-1"),
                                    ]),
                                ]),
                                html.H5("Orador 2"),
                                html.P("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora \
                                        voluptatem quasi doloremque rerum, nulla voluptate. Accusamus, tempora. \
                                        Consectetur tempora fuga quasi, cumque atque obcaecati quisquam dolorem \
                                        iste voluptatum dolorum nostrum.", className="card-text"),
                            ]),
                        ],
                    )
                ]),


                dbc.Col(className="col-12 col-md-6 col-lg-4 mb-4", children=[

                    dbc.Card([
                            dbc.CardImg(src="assets/speakers/elefante.jpg", top=True),
                            dbc.CardBody([
                                html.Div(className="badges", children=[
                                    html.Span([
                                        dbc.Badge("JavaScript", color="warning", className="me-1"),
                                        dbc.Badge("Spark", color="success", className="me-1"),
                                    ]),
                                ]),
                                html.H5("Orador 3"),
                                html.P("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora \
                                        voluptatem quasi doloremque rerum, nulla voluptate. Accusamus, tempora. \
                                        Consectetur tempora fuga quasi, cumque atque obcaecati quisquam dolorem \
                                        iste voluptatum dolorum nostrum.", className="card-text"),
                            ]),
                        ],
                    )
                ]),


                dbc.Col(className="col-12 col-md-6 col-lg-4 mb-4", children=[

                    dbc.Card([
                            dbc.CardImg(src="assets/speakers/zebra.jpg", top=True),
                            dbc.CardBody([
                                html.Div(className="badges", children=[
                                    html.Span([
                                        dbc.Badge("JavaScript", color="warning", className="me-1"),
                                        dbc.Badge("Spark", color="success", className="me-1"),
                                    ]),
                                ]),
                                html.H5("Orador 4"),
                                html.P("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora \
                                        voluptatem quasi doloremque rerum, nulla voluptate. Accusamus, tempora. \
                                        Consectetur tempora fuga quasi, cumque atque obcaecati quisquam dolorem \
                                        iste voluptatum dolorum nostrum.", className="card-text"),
                            ]),
                        ],
                    )
                ]),


                dbc.Col(className="col-12 col-md-6 col-lg-4 mb-4", children=[

                    dbc.Card([
                            dbc.CardImg(src="assets/speakers/snake.jpg", top=True),
                            dbc.CardBody([
                                html.Div(className="badges", children=[
                                    html.Span([
                                        dbc.Badge("JavaScript", color="warning", className="me-1"),
                                        dbc.Badge("Spark", color="success", className="me-1"),
                                    ]),
                                ]),
                                html.H5("Orador 5"),
                                html.P("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora \
                                        voluptatem quasi doloremque rerum, nulla voluptate. Accusamus, tempora. \
                                        Consectetur tempora fuga quasi, cumque atque obcaecati quisquam dolorem \
                                        iste voluptatum dolorum nostrum.", className="card-text"),
                            ]),
                        ],
                    )
                ]),


                dbc.Col(className="col-12 col-md-6 col-lg-4 mb-4", children=[

                    dbc.Card([
                            dbc.CardImg(src="assets/speakers/paloma.jpg", top=True),
                            dbc.CardBody([
                                html.Div(className="badges", children=[
                                    html.Span([
                                        dbc.Badge("JavaScript", color="warning", className="me-1"),
                                        dbc.Badge("Spark", color="success", className="me-1"),
                                    ]),
                                ]),
                                html.H5("Orador 6"),
                                html.P("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora \
                                        voluptatem quasi doloremque rerum, nulla voluptate. Accusamus, tempora. \
                                        Consectetur tempora fuga quasi, cumque atque obcaecati quisquam dolorem \
                                        iste voluptatum dolorum nostrum.", className="card-text"),
                            ]),
                        ],
                    )
                ]),


            ]),
        ])
    ]),












    ############################################## interior ##############################################



    html.Br(),
    html.H4("Main", className="sub_title"),
    html.Br(),






    ############################################### footer ###############################################
        
    dbc.Container([

        dbc.Row(children=[

            dbc.Col(children=[dbc.NavItem(dbc.NavLink("Preguntas frecuentes", href="#"))], className="col-12 col-lg"),
            dbc.Col(children=[dbc.NavItem(dbc.NavLink("Contactenos", href="#"))], className="col-12 col-lg"),
            dbc.Col(children=[dbc.NavItem(dbc.NavLink("Prensa", href="#"))], className="col-12 col-lg"),
            dbc.Col(children=[dbc.NavItem(dbc.NavLink("Conferencias", href="#"))], className="col-12 col-lg"),
            dbc.Col(children=[dbc.NavItem(dbc.NavLink("Terminos y condiciones", href="#"))], className="col-12 col-lg"),
            dbc.Col(children=[dbc.NavItem(dbc.NavLink("Privacidad", href="#"))], className="col-12 col-lg"),
            dbc.Col(children=[dbc.NavItem(dbc.NavLink("Estudiantes", href="#"))], className="col-12 col-lg"),

        ], className="row text-center"), 
        
    ], fluid=True, id="footer", className="pb-4 pt-4")


], fluid=True) 










################################################################################


##### callback para la haburguesa
# add callback for toggling the collapse on small screens
@app.callback(
     Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open















if __name__ == '__main__':
    app.run_server(debug=True)



###### NOTAS

# pt: padding top
# pb: padding botton