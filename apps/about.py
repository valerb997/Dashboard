import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from apps import env,ene,soc
from app import app
from app import server

layout= \
    html.Div([
    html.H1("About",
            style={'textAlign':'center'}),
])
