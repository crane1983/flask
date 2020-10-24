
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(
    children = [html.Div(style={'width': '49%', 'display': 'inline-block'},
    children=[
    html.H1(children='Hello Dash!'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
]
    ),
    html.Div(children =['Enter answer: ', dcc.Input(id='11', value = '1'),
                        dcc.Input(id='12', value = '2'),
                        dcc.Input(id='13', value = '3'),
                        dcc.Input(id='14', value = '4')],
             style={'width': '49%', 'display': 'inline-block'}),
    html.Div(children =['Enter answer: ', dcc.Input(id='21', value = '1'),
                        dcc.Input(id='22', value = '2'),
                        dcc.Input(id='23', value = '3'),
                        dcc.Input(id='24', value = '4')],
             style={'width': '49%', 'display': 'inline-block'}),
    html.Div('The 4gitth section')])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)
    #app.run_server(host='0.0.0.0', port=8080)