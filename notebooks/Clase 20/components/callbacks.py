from dash import html, Input, Output, State, callback
import dash_bootstrap_components as dbc


modals = html.Div(
    [
        dbc.Button("Quiero ser orador", outline=True, color="dark", className="me-1"),
        dbc.Button("Comprar tickets", id='modalCompra', className="btn-platzi"), 
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Comprar tickets"), close_button=True),
                dbc.Row(className="m-3", children=[
                        dbc.Label("Email: ", html_for="example-email-row", width=2),
                        dbc.Col(
                            dbc.Input(
                                type="email", id="example-email-row", placeholder="Enter email"
                            ), width=10
                        ),
                        dbc.Alert("You have a mail", color="warning", className="m-3"),  
                    ],
                ),

                dbc.ModalFooter([
                    dbc.Button("Cancel", id="close-centered", n_clicks=0, color="secondary", className="me-1"),
                    dbc.Button("Comprar", className="btn-platzi"),
                ]),
            ],
            id="modal-centered",
            centered=True,
            is_open=False,
        ),
    ]
)

@callback(
    Output("modal-centered", "is_open"),
    [Input("modalCompra", "n_clicks"), 
     Input("close-centered", "n_clicks")],
     # Input("close-centered", "n_clicks")],
    [State("modal-centered", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
