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
            html.H5(html.B("Description of the project 3")),
            id="collapse-button1",
            className="mb-3",
            color="primary",
            n_clicks=0,
            block=True,
            outline=True,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody([
                html.Div(str[1]),
                html.Div(str[3])]),
            color="primary",
            outline=True,),
            id="collapse1",
            is_open=False,
        ),
    ]
)
chapter_2 = html.Div(
    [
        dbc.Button(
            html.H5(html.B("Data cleaning and preparation")),
            id="collapse-button2",
            className="mb-3",
            color="secondary",
            n_clicks=0,
            block=True,
            outline=True,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody([
                html.Div(str[7]),
                html.Div(str[8]),
                html.Div(str[9]),
                html.Div(str[10]),
                html.Div(str[11]),
                html.Div(str[12]),
                html.Div(str[13]),
                html.Div(str[14]),
            ]),
            color="secondary",
            outline=True,),
            id="collapse2",
            is_open=False,
        ),
    ]
)
chapter_3 = html.Div(
    [
        dbc.Button(
            html.H5(html.B("Data display and interpretation")),
            id="collapse-button3",
            className="mb-3",
            color="success",
            n_clicks=0,
            block=True,
            outline=True,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody([
                html.Div(str[17]),
                html.Div(str[18]),
                html.Div(str[19]),
                html.Div(str[20]),
                html.Div(str[21]),
                html.Div(str[22]),
            ]),
            color="success",
            outline=True,),
            id="collapse3",
            is_open=False,
        ),
    ],
)
chapter_4 = html.Div(
    [ #25 to 69
        dbc.Button(
            html.H5(html.B("Feature selection")),
            id="collapse-button4",
            className="mb-3",
            color="warning",
            n_clicks=0,
            block=True,
            outline=True,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody([
                html.Div(str[25]),
                html.Div(str[26]),
                html.B("_" + str[27]),
                html.Div(str[28]),
                html.Div(str[29]),
                html.Div(str[30]),
                html.Div(str[31]),
                html.Div(str[32]),
                html.Div(str[33]),
                html.Div(str[34]),
                html.Div(str[35]),
                html.Div(str[36]),
                html.Div(str[37]),
                html.Div(str[38]),
                html.Div(str[39]),
                html.Div(str[40]),
                html.Div(str[41]),
                html.Div(str[42]),
                html.Div("_" + str[43]),
                html.Div(str[44]),
                html.Div(str[45]),
                html.Div(str[46]),
                html.Div(str[47]),
                html.Div(str[48]),
                html.Div(str[49]),
                html.Div(str[50]),
                html.Div(str[51]),
                html.Div(str[52]),
                html.Div(str[53]),
                html.Div(str[54]),
                html.Div(str[55]),
                html.Div(str[56]),
                html.Div(str[57]),
                html.Div(str[58]),
                html.Div("_"),
                html.Div(str[59]),
                html.Div(str[60]),
                html.Div(str[61]),
                html.Div(str[62]),
                html.Div(str[63]),
                html.Div(str[64]),
                html.Div(str[65]),
                html.Div(str[66]),
                html.Div(str[67]),
                html.Div(str[68]),
                html.Div(str[69]),
            ]),
            color="warning",
            outline=True,),
            id="collapse4",
            is_open=False,
        ),
    ],
)
chapter_5 = html.Div(
    [
        dbc.Button(
            html.H5(html.B("Modeling and forecast")),
            id="collapse-button5",
            className="mb-3",
            color="danger",
            n_clicks=0,
            block=True,
            outline=True,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody([
                html.Div(str[71]),
                html.Div(str[72]),
                html.Div(str[73]),
                html.Div(str[74]),
            ]),
            color="danger",
            outline=True),
            id="collapse5",
            is_open=False,
        ),
    ],
)


layout= \
    html.Div([
    html.H1("About",
            style={'textAlign':'center'}),
    html.H6("This project has been developed by Andrea Borgo and Valeria Bona, Instituto Superior Técnico, Universidade de Lisboa",
            style={'textAlign':'center'}),
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