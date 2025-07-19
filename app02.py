import dash
from dash import html

app = dash.Dash(__name__)
server = app.server  # Heroku precisa disso

app.layout = html.Div([
    html.H1("Olá, mundo do Dash no Heroku!")
])
