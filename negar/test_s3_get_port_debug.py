# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 21:18:32 2022

@author: negar
"""

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import os
import boto3
#from Negara_accessKeys import access_key_ID, secret_access_key

client= boto3.client("s3")#, aws_access_key_id=access_key_ID, 
                     #aws_secret_access_key= secret_access_key)

response = client.get_object(Bucket='dat-files',Key='test.txt')
my_text = response['Body'].read()

#with open('https://dat-files.s3.us-west-1.amazonaws.com/test.txt') as f:
#with open(os.path.join(os.getcwd(), 'test.txt')) as f:
  #  my_text = f.readlines()


#my_text= open('./test.txt', 'r')#'the-zen-of-python.txt','r')

#s3 = boto3.client('s3')
#with open('test.txt','wb') as f:
 #   s3.download_fileobj('dat-files', 'test.txt', f)


app=dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP #MINTY
                                             ], #meta_tags=[{'name': 'viewport',
                          #  'content': 'width=device-width, initial-scale=1.0'}]
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
    app.run_server(host='0.0.0.0', port=8081)
    
   # app.run_server(port=1220, debug=True)
  #  port = int(os.environ.get("PORT"))
   # app.run_server(host='0.0.0.0', port)
    
    
    app.run_server(host='0.0.0.0', port=8080, debug=True)
  #  port = int(os.environ.get("PORT"))
 # app.run_server(host='0.0.0.0', port)
  