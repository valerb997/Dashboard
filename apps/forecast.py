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
df4=pd.read_csv(DATA_PATH.joinpath("model_estimation_IVorder.csv"))
df4err=pd.read_csv(DATA_PATH.joinpath("errors_IVorder.csv"))
df2=pd.read_csv(DATA_PATH.joinpath("model_estimation_IIorder.csv"))
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
# df4=pd.read_csv(DATA_PATH.joinpath("model_estimation_IVorder.csv"))
fig4sGB=px.scatter(df4, x="y_test", y="y_pred_GB")
fig4sGB.update_layout(
    title_text="4th order polynomial"
)
fig4sLR=px.scatter(df4, x="y_test", y="y_pred_LR")
fig4sLR.update_layout(
    title_text="4th order polynomial"
)
fig4lGB=px.line(df4,y=["y_pred_GB","y_test"])
fig4lGB.update_layout(
    title_text="4th order polynomial"
)
fig4lLR=px.line(df4, y=["y_pred_LR","y_test"])
fig4lLR.update_layout(
    title_text="4th order polynomial"
)

fig2sGB=px.scatter(df2, x="y_test", y="y_pred_GB")
fig2sGB.update_layout(
    title_text="2nd order polynomial"
)
fig2sLR=px.scatter(df2, x="y_test", y="y_pred_LR")
fig2sLR.update_layout(
    title_text="2nd order polynomial"
)
fig2lGB=px.line(df2,y=["y_pred_GB","y_test"])
fig2lGB.update_layout(
    title_text="2nd order polynomial"
)
fig2lLR=px.line(df2, y=["y_pred_LR","y_test"])
fig2lLR.update_layout(
    title_text="2nd order polynomial"
)
# table4=px.scatter(df4, x=)
# fig2s=px.scatter()
# fig2l=px.line
# table2=
# figrs=px.scatter()
# figrl=px.line()
# tabler=
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
                                  style={'backgroundColor': 'black', 'color': 'black'},
                                multi=True),
                        )]),
    dbc.Row(dcc.Graph(id='fore_graph')),
    dbc.Row(html.H2("Model validation and errors")),
    dbc.Row(html.H4("Line plots - Linear Regression")),
        dbc.Row([
            dbc.Col(dcc.Graph(id='enr_graph',
                           figure=fig4lLR,
                           )),
            dbc.Col(dcc.Graph(id='enr_graph',
                           figure=fig2lLR,
                           )),
            # dbc.Col(table4GB),
        ]),

        dbc.Row(html.H4("Line plots - Gradient Boosting")),
        dbc.Row([
            dbc.Col(dcc.Graph(id='enr_graph',
                           figure=fig4lGB,
                           )),
            dbc.Col(dcc.Graph(id='enr_graph',
                           figure=fig2lGB,
                           )),
            # dbc.Col(table4GB),
        ]),
    dbc.Row(html.H4("Scatter plots - Linear Regression")),
        dbc.Row([
            dbc.Col(dcc.Graph(id='enr_graph',
                              figure=fig4sLR,
                              )),
            dbc.Col(dcc.Graph(id='enr_graph',
                              figure=fig2sLR,
                              )),
            # dbc.Col(table4GB),
        ]),
        dbc.Row(html.H4("Scatter plots - Gradient Boosting")),
        dbc.Row([
            dbc.Col(dcc.Graph(id='enr_graph',
                              figure=fig4sGB,
                              )),
            dbc.Col(dcc.Graph(id='enr_graph',
                              figure=fig2sGB,
                              )),
        ]),
        dbc.Row(html.H4("Error tables")),
])

@app.callback(
    Output(component_id='fore_graph', component_property='figure'),
    [Input(component_id='f_dropdown', component_property='value'),
     # Input(component_id="ene_slider",component_property="value"),
     ]
)

def update_graph(f_dropdown):
    chart = px.line(data_frame=df, y=f_dropdown, x=l[0],template="plotly_dark")
    chart.update_layout(
        yaxis_title="Electricity consumption [GWh]",
        legend_title="Legend",
    )
    return chart