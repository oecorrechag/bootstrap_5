from dash import Dash, html, Input, Output, State, html
import dash_bootstrap_components as dbc

from components.callbacks import modals

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
                        href="/",
                        style={"textDecoration": "none"},
                    ),
                    dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                    dbc.Collapse(className="navbar", children=[

                        dbc.Row([dbc.Col(children=[dbc.NavItem(dbc.NavLink("Conferencia", href="#main"))])],
                                    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0", align="center"),

                        dbc.Row([dbc.Col(children=[dbc.NavItem(dbc.NavLink("Oradores", href="#speakers"))])],
                                    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0", align="center"),

                        dbc.Row([dbc.Col(children=[dbc.NavItem(dbc.NavLink("Lugar y fecha", href="#place-time"))])],
                                    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0", align="center"),

                        dbc.Row([dbc.Col(children=[dbc.NavItem(dbc.NavLink("Conviertete en orador", href="conviertete-en-orador"))])],
                                    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0", align="center"),

                        dbc.Row([dbc.Col(children=[dbc.NavItem(dbc.NavLink("Tickets", id='modal_comprar', href="#", className="text-platzi"))])],
                                    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0", align="center"),

                    ], id="navbar-collapse", is_open=False, navbar=True,
                    ),
                ]
            ),
            color="dark",
            dark=True,
        ), 

    ], className='fixed-top'),


    ################################################ Main ################################################


    html.Br(),html.Br(),html.Br(),

    dbc.Container(id='main', className='container-fluid', children=[  

        dbc.Container(className='carousel-inner px-0', children=[ 

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

            html.Div(className='overlay carousel-caption', children=[

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
                        modals,

                        ], width={"size": 6, "offset": 6}),

                    ], className="row text-center"), 
                ]),
                
            ]),

        ], fluid=True),

    ], fluid=True),



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


    ########################################### place and date ###########################################

    html.Div(id='place-time', children=[
        dbc.Container([
            dbc.Row(children=[

                dbc.Col(className="col-12 col-lg-6 pl-0 pr-0", children=[
                    html.Img(src="assets/images/honolulu.jpeg")
                ]),


                dbc.Col(className="col-12 col-lg-6 pt-4 pb-4", children=[
                    html.H2("Conferencias 2030"),
                    html.P("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora \
                            voluptatem quasi doloremque rerum, nulla voluptate. Accusamus, tempora. \
                            Consectetur tempora fuga quasi, cumque atque obcaecati quisquam dolorem \
                            iste voluptatum dolorum nostrum.", className="card-text"),
                    dbc.Button("Conoce más", href="https://es.wikipedia.org/wiki/Honolulu", outline=True, color="light", className="me-1"),
                ]),
            ]),
        ], fluid=True) 
    ]),



    ############################################ be a speaker ############################################

    html.Div(id='conviertete-en-orador', className="pt-3 pb-3", children=[
        dbc.Container([

            dbc.Row(children=[

                dbc.Col(className="col text-uppercase text-center", children=[
                    html.Small("Conviertete en un"),
                    html.H2("Orador"),
                ]),

            ]),


            dbc.Row(children=[

                dbc.Col(className="col text-center", children=[
                    html.P(["Anotate como orador para dar una ", 
                    html.Span("charla ignite", id="tooltip",style={"cursor": "pointer"},), 
                    " Cuentanos de que quienes hablar?"]),
                    dbc.Tooltip("talks of mins", target="tooltip"),
                ]),

            ]),

            dbc.Row(children=[

                dbc.Col(className="col col-md-10 offset-md-1 col-lg-8 offset-lg-2 pt-2", children=[

                    dbc.Row(children=[

                        dbc.Col(className="form-label col-12 col-md-6", children=[

                            dbc.Input(type="text", id="first_name", className="form-control", placeholder="First name",),

                        ]),

                        dbc.Col(className="form-label col-12 col-md-6", children=[

                            dbc.Input(type="text", id="last_name", className="form-control", placeholder="Last name",),

                        ]),

                    ]),

                    dbc.Row(children=[
                        dbc.Col([

                            html.Div(
                                [
                                    dbc.Textarea(className="mb-3", placeholder="Sobre tu charla"),
                                    html.Small(["Recuerde poner ",
                                    html.Span("titulo", id="tooltip2",style={"cursor": "pointer"},), 
                                    '.']),
                                    dbc.Tooltip("talk name", target="tooltip2"),
                                ]
                            ),

                        ]),
                    ]),


                    dbc.Row(children=[
                        dbc.Col([
                            dbc.Button("Enviar", className="btn btn-platzi w-100"), 
                        ]),
                    ]),

                ]),
            ]),
        ]),
    ]),











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
        
    ], fluid=True, id="footer", className="pb-4 pt-4"),



], fluid=True, class_name='home') 


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