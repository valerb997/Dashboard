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
df=pd.read_csv(DATA_PATH.joinpath("deforest.csv"))
l=df.columns.values.tolist()
fig = px.scatter(data_frame=df, y=l[2], x=l[1], template="plotly_dark")
fig.update_layout(
    legend_title="Legend",
)
complex_card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("About this plot", className="card-title"),
            html.P(
                "This scatter plot shows a very high negative correlation between electricity consumption "
                "and the loss of forest area. A useful method to evaluate the degree of correlation between "
                " the two variables is by estimating the correlation coefficients (in this case the Pearson, the "
                "Spearman and the Kendall coefficients, which correspond to -0.939, -0.991 and -0.949 respectively). "
                " These three factors use different methods to estimate the correlation between the two variables and all of them show results above"
                " 90%, meaning that there is a strong link between energy consumption and deforestation ",
                className="card-text",
            ),
            dbc.CardLink("Global Forest Watch", href="https://www.globalforestwatch.org/dashboards/country/SEN/?category=summary&dashboardPrompts=eyJzaG93UHJvbXB0cyI6dHJ1ZSwicHJvbXB0c1ZpZXdlZCI6W10sInNldHRpbmdzIjp7Im9wZW4iOmZhbHNlLCJzdGVwSW5kZXgiOjAsInN0ZXBzS2V5IjoiIn0sIm9wZW4iOnRydWUsInN0ZXBzS2V5IjoiZG93bmxvYWREYXNoYm9hcmRTdGF0cyJ9&location=WyJjb3VudHJ5IiwiU0VOIl0%3D&map=eyJjZW50ZXIiOnsibGF0IjoxMy44NjAzNDQ4Njk2MTM2NjIsImxuZyI6LTEyLjg4NjAxNzI1MDU4NzY3Mn0sInpvb20iOjUuMjE0NjY1NjE3NDgwMywiY2FuQm91bmQiOmZhbHNlLCJkYXRhc2V0cyI6W3sib3BhY2l0eSI6MC43LCJ2aXNpYmlsaXR5Ijp0cnVlLCJkYXRhc2V0IjoicHJpbWFyeS1mb3Jlc3RzIiwibGF5ZXJzIjpbInByaW1hcnktZm9yZXN0cy0yMDAxIl19LHsiZGF0YXNldCI6InBvbGl0aWNhbC1ib3VuZGFyaWVzIiwibGF5ZXJzIjpbImRpc3B1dGVkLXBvbGl0aWNhbC1ib3VuZGFyaWVzIiwicG9saXRpY2FsLWJvdW5kYXJpZXMiXSwiYm91bmRhcnkiOnRydWUsIm9wYWNpdHkiOjEsInZpc2liaWxpdHkiOnRydWV9LHsiZGF0YXNldCI6InRyZWUtY292ZXItbG9zcyIsImxheWVycyI6WyJ0cmVlLWNvdmVyLWxvc3MiXSwib3BhY2l0eSI6MSwidmlzaWJpbGl0eSI6dHJ1ZSwidGltZWxpbmVQYXJhbXMiOnsic3RhcnREYXRlIjoiMjAwMi0wMS0wMSIsImVuZERhdGUiOiIyMDIwLTEyLTMxIiwidHJpbUVuZERhdGUiOiIyMDIwLTEyLTMxIn0sInBhcmFtcyI6eyJ0aHJlc2hvbGQiOjMwLCJ2aXNpYmlsaXR5Ijp0cnVlfX1dfQ%3D%3D"),
        ]
    ),
    style={"width": "18rem"},
)
layout= \
html.Div([
    html.H1("Deforestation", style={'textAlign':'center'}),
    dbc.Row([dbc.Col(dcc.Graph(id='enr_graph',
                           figure=fig,
                            style={'width': '150vh'}
                           )),
             dbc.Col(complex_card)]),
    #write layout here
])


if __name__ == '__main__':
    app.run_server()