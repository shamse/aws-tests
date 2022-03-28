import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import os

app=dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP #MINTY]
              #, meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}]
              )
                                                            
app.layout = dbc.Container([html.Div([
    dbc.Row([dbc.Col([html.Div([html.H6("INAAA", className="text-center bg-light text-nowrap text-primary border font-weight-bolder mt-5"),#Pseudo-Sommerfeld m/(Pa.s)"),
                                dcc.Markdown(id='out_var')],className="text-center"),]),
             ]),
    ]),])

@app.callback(
    [
    Output("out_var", "children")
    ],
    
    [Input('out_var', 'children')]
    )

def write_text(texts):
    return[str(my_text)]

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080)
