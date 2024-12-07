import dash
from dash import html, dcc, Dash
import plotly.express as px

px.defaults.template = "ggplot2"

# External CSS
external_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"]
# Initialize Dash app
app = Dash(__name__, pages_folder='Pages', use_pages=True, external_stylesheets=external_css)

# App layout
app.layout = html.Div([
    html.Br(),
    html.P('User Behavior Dashboard', className="text-dark text-center fw-bold fs-1"),
    html.Div(
        children=[
            dcc.Link(page['name'], href=page["relative_path"], className="btn btn-dark m-2 fs-5")
            for page in dash.page_registry.values()
        ],
        className="text-center"
    ),
    dash.page_container
], className="col-8 mx-auto")
# Run the app
if __name__ == '__main__':
    app.run(debug=True)