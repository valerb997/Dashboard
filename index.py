import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from apps import env,ene,soc
from app import app
from app import server
BS = "https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/solar/bootstrap.min.css"
app = dash.Dash(external_stylesheets=[BS])
PLOTLY_LOGO="logo.png"
navbar= html.Div([
    dbc.NavbarSimple(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("Senegal Dashboard", className="ml-2",href="/")),
                    dbc.Col(dbc.NavItem(dbc.NavLink("Environment", href="/environment"))),
                    dbc.Col(dbc.NavItem(dbc.NavLink("Social", href="/social"))),
                    dbc.Col(dbc.NavItem(dbc.NavLink("Energy", href="/energy"))),
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
    html.Div(id="page-content", children=[])
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
                ]
    elif pathname == "/environment":
        return env.layout

    elif pathname == "/social":
        return soc.layout
    elif pathname =="/energy":
        return ene.layout


    # elif pathname =="/about":

    # If the user tries to reach a different page, return a 404 message


if __name__ == '__main__':
    app.run_server()