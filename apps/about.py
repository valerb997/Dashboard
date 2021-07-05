import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from apps import env,ene,soc
from app import app
from app import server
import docx2txt
my_text = docx2txt.process("DESCRIPTION OF THE PROJECT 3.docx")

s="\n"
for i in range(5):
    s=s+"\n"
    my_text=my_text.replace(s, '\n')
new = list(filter(None, my_text))
str=""
for c in new:
    str=str+c
str=str.split("\n")
chapter_1 = html.Div(
    [
        dbc.Button(
            "Description of the project 3",
            id="collapse-button1",
            className="mb-3",
            color="info",
            n_clicks=0,
            block=True,
            outline=True,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody([
                html.Div(str[1]),
                html.Div(str[3])])),
            id="collapse1",
            is_open=False,
        ),
    ]
)
chapter_2 = html.Div(
    [
        dbc.Button(
            "Data cleaning and preparation",
            id="collapse-button2",
            className="mb-3",
            color="info",
            n_clicks=0,
            block=True,
            outline=True,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(str[1030:2625])),
            id="collapse2",
            is_open=False,
        ),
    ]
)
chapter_3 = html.Div(
    [
        dbc.Button(
            "Data display and interpretation",
            id="collapse-button3",
            className="mb-3",
            color="info",
            n_clicks=0,
            block=True,
            outline=True,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(str[2658:5047])),
            id="collapse3",
            is_open=False,
        ),
    ],
)
chapter_4 = html.Div(
    [
        dbc.Button(
            "Feature selection",
            id="collapse-button4",
            className="mb-3",
            color="info",
            n_clicks=0,
            block=True,
            outline=True,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(str[5067:6909])),
            id="collapse4",
            is_open=False,
        ),
    ],
)
chapter_5 = html.Div(
    [
        dbc.Button(
            "Modeling and forecast",
            id="collapse-button5",
            className="mb-3",
            color="info",
            n_clicks=0,
            block=True,
            outline=True,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(str[6932:])),
            id="collapse5",
            is_open=False,
        ),
    ],
)


layout= \
    html.Div([
    html.H1("About",
            style={'textAlign':'center'}),
    html.H6("This project has been developed by Andrea Borgo and Valeria Bona, Instituto Superior Técnico, Universidade de Lisboa"),
    dbc.Row(chapter_1),
    dbc.Row(chapter_2),
    dbc.Row(chapter_3),
    dbc.Row(chapter_4),
    dbc.Row(chapter_5)
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

@app.callback(
    Output("collapse3", "is_open"),
    [Input("collapse-button3", "n_clicks")],
    [State("collapse3", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse4", "is_open"),
    [Input("collapse-button4", "n_clicks")],
    [State("collapse4", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
@app.callback(
    Output("collapse5", "is_open"),
    [Input("collapse-button5", "n_clicks")],
    [State("collapse5", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open