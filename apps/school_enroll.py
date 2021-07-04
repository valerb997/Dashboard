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
df=pd.read_csv(DATA_PATH.joinpath("School_enroll.csv"))
l=df.columns.values.tolist()
fig = px.scatter(data_frame=df, y=l[2:5], x=l[1], template="plotly_dark")
fig.add_vline(x=128, line_width=3, line_dash="dash", line_color="green")
layout= \
html.Div([
    html.H1("Hello world!"),
    dbc.Row([dbc.Col(dcc.Graph(id='enr_graph',
                           figure=fig
                           # {
                           #      'data': [
                           #          {'x': df[l[1]], 'y': df[l[2]], 'type': 'scatter', 'name': 'SF'},
                           #          {'x': df[l[1]], 'y': df[l[3]], 'type': 'scatter', 'name': u'Montréal'},
                           #          {'x': df[l[1]], 'y': df[l[4]], 'type': 'scatter', 'name': "Male + Female"},
                           #              ],
                           #      "layout": dict(
                           #         plot_bgcolor="#171b26",
                           #         paper_bgcolor="#171b26",
                           #     ),
                           # },
                           ))]),
    #write layout here
])

# @app.callback(
#     Output(component_id='enr_graph', component_property='figure'),
#     [Input(component_id='dummy', component_property='id'),
#      ]
# )
#
# def update_graph():
#     chart = px.scatter(data_frame=df, y=l[3], x=l[1], template="plotly_dark")
#     return chart



if __name__ == '__main__':
    app.run_server()