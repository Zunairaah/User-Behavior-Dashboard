import pandas as pd
import dash
from dash import Dash, html, dash_table, dcc
import plotly.graph_objects as go

dash.register_page(__name__, path='/dataset', name="Dataset")

data = pd.read_csv('H:\\Zunaira\\Machine Learning\\User Behavior Dashboard\\user_behavior_dataset.csv')

layout = html.Div(children=[
    html.Br(),
    dash_table.DataTable(
        data=data.to_dict('records'),
        page_size=20,
        style_cell={"background-color": "lightgrey", "border": "solid 1px white", "color": "black"},
        style_header={"background-color": "dodgerblue", "font-weight": "bold", "color": "black"}
    ),
])