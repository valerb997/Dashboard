#you'll need 4%increment, polyval(2 and 4 grade),
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import pathlib
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from apps import env,ene,soc
from app import app
from app import server

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df=pd.read_csv(DATA_PATH.joinpath("data_to_plot.csv"))
l=df.columns.values.tolist()

layout= \
    html.Div([
    dbc.Row(html.H1("Energy consumption forecast",
            style={'textAlign':'center'})),
    dbc.Row([dbc.Col(dcc.Dropdown(id='f_dropdown', placeholder='(De)select which model you want to see...',
                                     options=[{'label': l[1], 'value': l[1]},
                                              {'label': l[2], 'value': l[2]},
                                              {'label': l[3], 'value': l[3]},
                                              {'label': l[4], 'value': l[4]},
                                              ],
                                  value=l[1:5],
                                  searchable=True,
                                multi=True),
                        width={'size': 3, 'order': 1}
                        )]),
    dbc.Row(dcc.Graph(id='fore_graph')),
])

@app.callback(
    Output(component_id='fore_graph', component_property='figure'),
    [Input(component_id='f_dropdown', component_property='value'),
     # Input(component_id="ene_slider",component_property="value"),
     ]
)

def update_graph(f_dropdown):
    chart = px.line(data_frame=df, y=f_dropdown, x=l[0],template="plotly_dark")
    return chart