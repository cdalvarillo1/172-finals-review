import webbrowser #allows us to open a web browser when running the code

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Input, Output, State
from dash.exceptions import PreventUpdate
from utilities import generateFibonacci, getFactorial

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])
# dash.Dash () creates the application
#__name__ tells python the name of the file being executed/made the module
# external_stylesheets: loads Bootstrap style sheets


app.title = "My First Dash App"

#add brackets inside the element when you have multiple elements
#this creates a list of elements
app.layout = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader("First Dash App"),
                dbc.CardBody(
                    [
                        html.Div(
                            [
                                dbc.Label("Number"),
                                dbc.Input(
                                    placeholder="Place number here",
                                    type="text",
                                    id='num_input'
                                ),
                                dbc.FormText("Nonnegative numbers are not allowed.")
                            ]
                        ),
                        html.Div(
                            [
                                dbc.Label("Process"),
                                dbc.Select(
                                    id="process_select",
                                    options =[
                                        {"label":"Get Factorial","value":1},
                                        {"label":"Get Fibonacci sequence","value":2},
                                    ]

                                ),
                                dbc.FormText("Select an operation") 
                            ]
                        ),
                        dbc.Button(
                            "Calculate!",
                            id='btn_calculate',
                            color='primary',
                            n_clicks=0
                        ),
                        html.Div(
                            id='output_area'
                        )
                    ],
                ),
                dbc.FormText("This is the footer")
            ],
            style={"width":"18rem"},
        )
    ]
)

@callback(
    [
        Output('output_area','children')
    ],
    [
        Input('btn_calculate','n_clicks')
    ],
    [
        State('num_input','value'),
        State('process_select','value')
    ]
)
def calculateResults(btn_calculate, num_input, process_select):
    if btn_calculate > 0:
        num_input = int(num_input)
        process_select = int(process_select)
        if process_select == 1:
            factorial_value = getFactorial(num_input)
            output_val = str(factorial_value)
        elif process_select == 2:
            fib_sequence = generateFibonacci(num_input)
            fib_sequence_str = [str(i) for i in fibonacci_sequence],
            output_val = ",".join(fib_sequence_str)
            #joins a lot of strings together
        else:
            raise PreventUpdate
    else:
        raise PreventUpdate
    return[output_val]


# to run the server
if __name__ == '__main__':
    #instruct python that this is the file that was directly started
    webbrowser.open('http://127.0.0.1:8050', autoraise=True)
    app.run()