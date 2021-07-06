import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from apps import env,ene,soc,about,forecast, school_enroll, deforest, life_expect
from app import app
from app import server
# BS = "https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/solar/bootstrap.min.css"
# app = dash.Dash(external_stylesheets=[BS])

import base64
bus_png = 'DSC_0011.jpg'
bus_base64 = base64.b64encode(open(bus_png, 'rb').read()).decode('ascii')
ppl_png = 'DSC_0079.jpg'
ppl_base64 = base64.b64encode(open(ppl_png, 'rb').read()).decode('ascii')
ferry_png = 'DSC_0147.jpg'
ferry_base64 = base64.b64encode(open(ferry_png, 'rb').read()).decode('ascii')
flag_png = 'mappa_senegal_2.png'
flag_base64 = base64.b64encode(open(flag_png, 'rb').read()).decode('ascii')
navbar= html.Div([
    dbc.NavbarSimple(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(dbc.NavbarBrand("Senegal Dashboard", className="ml-2",href="/")),
                    dbc.Col(dbc.NavItem(dbc.NavLink("Environment", href="/environment"))),
                    dbc.Col(dbc.NavItem(dbc.NavLink("Social", href="/social"))),
                    dbc.Col(dbc.NavItem(dbc.NavLink("Energy", href="/energy"))),
                    dbc.Col(dbc.DropdownMenu(
                        children=[
                            dbc.DropdownMenuItem("Energy consumption vs", header=True),
                            dbc.DropdownMenuItem("School Enrollment", href="/correlations/schoolenrollment"),
                            dbc.DropdownMenuItem("Deforestation", href="/correlations/deforestation"),
                            dbc.DropdownMenuItem("Life expectancy", href="/correlations/life_expectancy"),
                        ],
                        nav=True,
                        in_navbar=True,
                        label="Correlations",
                    )),
                    dbc.Col(dbc.NavItem(dbc.NavLink("Forecast", href="/forecast"))),
                    dbc.Col(dbc.NavItem(dbc.NavLink("About", href="/about"))),
                ],
                align="left",
                no_gutters=True,
            ),
        ),
    ],
    color="dark",
    dark=True,
)
    ])

app.layout=\
    html.Div([
    dcc.Location(id="url", refresh=False),
    navbar,
    html.Div(id="page-content", children=[]),
dbc.Row(dbc.Card([dbc.CardBody("This page was created by Andrea Borgo and Valeria Bona, ist1100834 and ist1100833, Instituto Superior Técnico, Universidade de Lisboa")
                  ])),
    

])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)

def render_page_content(pathname):
    if pathname == "/":
        return [
                html.H1('Welcome to our Senegal Dashboard!',
                        style={'textAlign':'center'}),
            html.Div([
                html.Img(src='data:image/png;base64,{}'.format(flag_base64), width="1500",height="600"),
                dbc.Row([dbc.Col(html.Img(src='data:image/png;base64,{}'.format(bus_base64), width="1000", height="600")),
                        dbc.Col(html.Img(src='data:image/png;base64,{}'.format(ppl_base64), width="1000", height="600"))
                        ]),
                html.Img(src='data:image/png;base64,{}'.format(ferry_base64), width="1000", height="600")],
            style={'textAlign': 'center'})
                ]
    elif pathname == "/environment":
        return env.layout

    elif pathname == "/social":
        return soc.layout
    elif pathname =="/energy":
        return ene.layout
    elif pathname =="/about":
        return about.layout
    elif pathname =="/forecast":
        return forecast.layout
    elif pathname =="/correlations/schoolenrollment":
        return school_enroll.layout
    elif pathname =="/correlations/deforestation":
        return deforest.layout
    elif pathname =="/correlations/life_expectancy":
        return life_expect.layout


    # If the user tries to reach a different page, return a 404 message


if __name__ == '__main__':
    app.run_server()