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
df=pd.read_csv(DATA_PATH.joinpath("WorldBank_social+.csv"))
l=df.columns.values.tolist()

layout= \
html.Div([
dbc.Row(dbc.Col(html.H1("Social data"),
                style={'textAlign':'center'})),
dbc.Row(dbc.Col(html.H5("Select a feature to plot it on the graph"),
                style={'textAlign':'center'})),
dbc.Row([dbc.Col(dcc.Dropdown(id='f_dropdown', placeholder='Select a Feature...',
                                     options=[{'label': l[1], 'value': l[1]},
                                              {'label': l[2], 'value': l[2]},
                                              {'label': l[3], 'value': l[3]},
                                              {'label': l[4], 'value': l[4]},
                                              {'label': l[5], 'value': l[5]},
                                              {'label': l[6], 'value': l[6]},
                                              {'label': l[7], 'value': l[7]},
                                              {'label': l[8], 'value': l[8]},
                                              {'label': l[9], 'value': l[9]},
                                              {'label': l[10], 'value': l[10]},
                                              {'label': l[11], 'value': l[11]},
                                              {'label': l[12], 'value': l[12]},
                                              {'label': l[13], 'value': l[13]},
                                              {'label': l[14], 'value': l[14]},
                                              {'label': l[15], 'value': l[15]},
                                              {'label': l[16], 'value': l[16]},
                                              ],
                                  value=l[1],
                                  searchable=True,
                                  style={'backgroundColor': 'black', 'color': 'black'},
                                multi=True),
                        width={'size': 3, 'order': 1}
                        )]),
dbc.Row([dbc.Col(dcc.Graph(id='soc_graph'))]),
dbc.Row(dbc.Col(html.H6("Please note that not all the data were available in the same time frame: the unavailable data are equal to 0")))
])

@app.callback(
    Output(component_id='soc_graph', component_property='figure'),
    [Input(component_id='f_dropdown', component_property='value'),
     ]
)

def update_graph(f_dropdown):
    chart = px.line(data_frame=df, y=f_dropdown, x=l[0],template="plotly_dark")
    return chart

if __name__ == '__main__':
    app.run_server()