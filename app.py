import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Olá, mundo!'),
    html.P('Meu primeiro Dash no Heroku.')
])

server = app.server  # <- ESSENCIAL PARA O HEROKU
