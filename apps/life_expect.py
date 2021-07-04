import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import pathlib
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df=pd.read_csv(DATA_PATH.joinpath("life_expect.csv"))
l=df.columns.values.tolist()
x= 103
y= 59
a=[103,103,72]
b=[59,39,59]
fig = px.scatter(data_frame=df, y=l[2], x=l[1], template="plotly_dark")
fig.add_vline(x=x, line_width=1, line_dash="dash", line_color="grey")
fig.add_hline(y=y,line_width=1, line_dash="dash", line_color="grey")
fig.add_trace(go.Scatter(x=a, y=b,
                    mode='markers',
                    name='point'))
complex_card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Title", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text",
            ),
            dbc.CardLink("Card link", href="#"),
            dbc.CardLink("External link", href="https://google.com"),
        ]
    ),
    style={"width": "18rem"},
)
layout= \
html.Div([
    html.H1("Hello world!", style={'textAlign':'center'}),
    dbc.Row([dbc.Col(dcc.Graph(id='enr_graph',
                           figure=fig,
                            style={'width': '150vh'}
                           )),
             dbc.Col(complex_card)]),
    #write layout here
])


if __name__ == '__main__':
    app.run_server()