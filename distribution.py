import pandas as pd
import dash
from dash import html, dcc, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/distribution', name="Distribution")

data = pd.read_csv('H:\\Zunaira\\Machine Learning\\User Behavior Dashboard\\user_behavior_dataset.csv')

# Histogram
def userID_graph(col_name="User ID"):
    return px.histogram(data_frame=data, x=columns, height=600)

# Widgets
columns = ["App Usage Time (min/day)", "Screen On Time (hours/day)", 
           "Battery Drain (mAh/day)", "Number of Apps Installed", "Data Usage (MB/day)"]
dd = dcc.Dropdown(id="dist_column", options=[{"label": col, "value": col} for col in columns], 
                  value=columns[0], clearable=False)  # Default to the first column

# Page Layout
layout = html.Div(children=[
    html.Br(),
    html.P("Select Column"),
    dd,
    dcc.Graph(id="histogram")
])

# Callbacks
@callback(Output("histogram", "figure"), [Input("dist_column", "value")])
def update_histogram(dist_column):
    return userID_graph(dist_column)  # Use the correct function