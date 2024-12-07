import pandas as pd
import dash
from dash import html, dcc, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/bar_chart', name="Categorical")

# Load Data
data = pd.read_csv('H:\\Zunaira\\Machine Learning\\User Behavior Dashboard\\user_behavior_dataset.csv')

# Bar Graph Function
def generate_bar_chart(column):
    # Calculate frequency counts for the selected column
    category_counts = data[column].value_counts().sort_index()
    return px.bar(
        x=category_counts.index, 
        y=category_counts.values, 
        labels={'x': column, 'y': 'Count'}, 
        title=f"Distribution of {column}",
        height=600
    )

# Dropdown Widget
columns = ["Device Model", "Operating System", "Gender", "User Behavior"]
dd = dcc.Dropdown(
    id="cate_col",  # Correct ID matches the Input below
    options=[{"label": col, "value": col} for col in columns], 
    value=columns[0], 
    clearable=False  # Default to the first column
)

# Page Layout
layout = html.Div(children=[
    html.Br(),
    html.P("Select Column"),
    dd,
    dcc.Graph(id="bargraph")
])

# Callback for Updating Bar Graph
@callback(Output("bargraph", "figure"), [Input("cate_col", "value")])  # Correct Input ID
def update_bargraph(cate_column):
    return generate_bar_chart(cate_column)  # Generate and return bar chart
