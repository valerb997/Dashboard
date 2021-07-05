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
x= 110
y= 60
a=[x,x,72]
b=[y,39,y]
fig = px.scatter(data_frame=df, y=l[2], x=l[1], template="plotly_dark")
fig.add_vline(x=x, line_width=1, line_dash="dash", line_color="grey")
fig.add_hline(y=y,line_width=1, line_dash="dash", line_color="grey")
fig.add_trace(go.Scatter(x=a, y=b,
                    mode='markers',
                    name='point'))
fig.update_layout(
    legend_title="Legend",
)
complex_card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("About this plot", className="card-title"),
            html.P(
                "Similarly to the school enrollment scatter plot, also between electricity consumption and "
                "life expectancy we can define a critical value which determines a change of the curve's slope."
                "In fact, below the average consumption of 110 kWh/capita, life expectancy can't exceed 60 years, "
                "while above this threshold people are expected to live more, but more consumption is required to"
                " significantly increase the years (after this point the curve is less steep) ",
                className="card-text",
            ),
            dbc.CardLink("World Bank Database", href="https://data.worldbank.org/indicator/SP.DYN.LE00.IN?locations=SN"),
        ]
    ),
    style={"width": "18rem"},
)
layout= \
html.Div([
    html.H1("Life expectancy", style={'textAlign':'center'}),
    dbc.Row([dbc.Col(dcc.Graph(id='enr_graph',
                           figure=fig,
                            style={'width': '150vh'}
                           )),
             dbc.Col(complex_card)]),
    #write layout here
])


if __name__ == '__main__':
    app.run_server()