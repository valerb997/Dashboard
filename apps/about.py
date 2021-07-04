import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from apps import env,ene,soc
from app import app
from app import server
chapter_1 = html.Div(
    [
        dbc.Button(
            "Open collapse",
            id="collapse-button1",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.H1("This content is hidden in the collapse"))),
            id="collapse1",
            is_open=False,
        ),
    ]
)
chapter_2 = html.Div(
    [
        dbc.Button(
            "Open collapse_2",
            id="collapse-button2",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody("This content is hidden in the collapse_2")),
            id="collapse2",
            is_open=False,
        ),
    ]
)


layout= \
    html.Div([
    html.H1("About",
            style={'textAlign':'center'}),
    chapter_1,
    chapter_2
])

@app.callback(
    Output("collapse1", "is_open"),
    [Input("collapse-button1", "n_clicks")],
    [State("collapse1", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
@app.callback(
    Output("collapse2", "is_open"),
    [Input("collapse-button2", "n_clicks")],
    [State("collapse2", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open