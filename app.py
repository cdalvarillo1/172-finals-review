import webbrowser #allows us to open a web browser when running the code

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

app.title = "My First Dash App"

app.layout = 
    html.Div( # isolated space on the layout
        "Hello World"
    )

# to run the server
if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050', autoraise=True)
    app.run()