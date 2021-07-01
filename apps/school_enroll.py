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

# PATH = pathlib.Path(__file__).parent
# DATA_PATH = PATH.joinpath("../datasets").resolve()
# df=pd.read_csv(DATA_PATH.joinpath("WorldBank_environment+.csv"))
# l=df.columns.values.tolist()

layout= \
html.Div([
    html.H1("Hello world!")
    #write layout here
])


if __name__ == '__main__':
    app.run_server()