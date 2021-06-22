import dash
from datetime import date
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df=pd.read_csv(DATA_PATH.joinpath("WorldBank_environment+.csv"))
l=df.columns.values.tolist()

layout= \
html.Div([
    dbc.Row(dbc.Col(html.H3("Environment data"))),
    dbc.Row(dbc.Col(html.H5("Select a feature to plot it on the graph"))),
    dbc.Row([dbc.Col(dcc.Dropdown(id='f_dropdown', placeholder='Select a Feature...',
                                     options=[{'label': l[1], 'value': l[1]},
                                              {'label': l[2], 'value': l[2]},
                                              {'label': l[3], 'value': l[3]},
                                              {'label': l[4], 'value': l[4]},
                                              ],
                                  value=l[1],
                                  searchable=True,
                                multi=True),
                        width={'size': 3, 'order': 1}
                        )]),
dbc.Row([dbc.Col(dcc.Graph(id='env_graph'))]),
dbc.Row(dbc.Col(html.H6("Please note that not all the data were available in the same time frame: the unavailable data are equal to 0")))
])

@app.callback(
    Output(component_id='env_graph', component_property='figure'),
    [Input(component_id='f_dropdown', component_property='value'),
     ]
)

def update_graph(f_dropdown):
    chart = px.line(data_frame=df, y=f_dropdown, x=l[0])
    return chart

if __name__ == '__main__':
    app.run_server()