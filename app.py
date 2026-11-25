import webbrowser #allows us to open a web browser when running the code

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])
# dash.Dash () creates the application
#__name__ tells python the name of the file being executed/made the module
# external_stylesheets: loads Bootstrap style sheets


app.title = "My First Dash App"

app.layout = html.Div( # isolated space on the layout
        "Hello World"
    )

# to run the server
if __name__ == '__main__':
    #instruct python that this is the file that was directly started
    webbrowser.open('http://127.0.0.1:8050', autoraise=True)
    app.run()