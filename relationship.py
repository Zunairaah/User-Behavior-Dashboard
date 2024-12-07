import pandas as pd
import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import plotly.express as px

# Load dataset
data = pd.read_csv('H:\\Zunaira\\Machine Learning\\User Behavior Dashboard\\user_behavior_dataset.csv')

# Register the page
dash.register_page(__name__, path='/relationship', name="Relationship")

# Scatter Plot function
def create_scatter_chart(x_axis="User Behavior", y_axis="User ID"):
    return px.scatter(data_frame=data, x=x_axis, y=y_axis, height=600)

# Columns for dropdowns
columns = [
    {"label": col, "value": col}
    for col in ["User ID", "Device Model", "Operating System", "App Usage Time (min/day)",
                "Screen On Time (hours/day)", "Battery Drain (mAh/day)", "Number of Apps Installed",
                "Data Usage (MB/day)", "Age", "Gender", "User Behavior"]
]

# Widgets
x_axis = dcc.Dropdown(id="x_axis", options=columns, value="User Behavior", clearable=False)
y_axis = dcc.Dropdown(id="y_axis", options=columns, value="User ID", clearable=False)

# Page Layout
layout = html.Div(children=[
    html.Br(),
    html.P("Select X-Axis:"),
    x_axis,
    html.P("Select Y-Axis:"),
    y_axis,
    dcc.Graph(id="scatter")
])

# Callbacks
@callback(Output("scatter", "figure"), [Input("x_axis", "value"), Input("y_axis", "value")])
def update_scatter_chart(x_axis, y_axis):
    return create_scatter_chart(x_axis, y_axis)