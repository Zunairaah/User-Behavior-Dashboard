import dash
from dash import html

dash.register_page(__name__, path='/', name="Introduction")

# Page Layout
layout = html.Div(children=[
        html.Div(children=[
                html.H2("Hey Friends!! I am Zunaira Hameed. Welcome to the User Behavior Dashboard"),
                html.P("This dashboard provides insights into user behavior by analyzing various device and usage metrics. It is built on a rich dataset that includes detailed information about users' app usage patterns, device specifications, and demographic data."),
                html.B("User ID:"),
                html.P("A unique identifier for each user."),
                html.B("Device Model:"),
                html.P("The specific device model being used."),
                html.B("Operating System:"),
                html.P("The operating system running on the device (e.g., Android, iOS)."),
                html.B("App Usage Time:"),
                html.P("The total time spent using apps per day (in minutes)."),
                html.B("Screen On Time:"),
                html.P("The duration the device screen is active per day (in hours)."),
                html.B("Battery Drain:"),
                html.P("The battery consumption per day (measured in mAh)."),
                html.B("Number of Apps Installed:"),
                html.P("The total apps installed on the user's device."),
                html.B("Data Usage:"),
                html.P("The internet consumption per day (in MB)."),
                html.B("Age:"),
                html.P("The age of the user."),
                html.B("Gender:"),
                html.P("The gender of each user (whether male or female)."),
                html.B("User Behavior:"),
                html.P("The target column which shows the user behavior based on all features."),
            ],
            className="bg-light p-4 m-2"
        )
    ]
)