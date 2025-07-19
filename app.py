import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Criando dados simples
df = pd.DataFrame({
    "Categoria": ["A", "B", "C", "D"],
    "Valores": [10, 15, 7, 12]
})

# Criando gráfico
fig = px.bar(df, x="Categoria", y="Valores", title="Gráfico de Teste")

# Criando o app
app = dash.Dash(__name__)
server = app.server  # Heroku precisa disso

# Layout do app
app.layout = html.Div(children=[
    html.H1("Meu primeiro Dash no GitHub", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])