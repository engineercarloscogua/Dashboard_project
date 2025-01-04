from dash import html, dcc
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Datos ficticios para la gráfica
np.random.seed(42)
df = pd.DataFrame({
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
    "Ingresos": np.random.randint(20000, 50000, 5),
    "Gastos": np.random.randint(15000, 40000, 5)
})

# Gráfica de líneas
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["Mes"], y=df["Ingresos"], mode="lines+markers", name="Ingresos", line=dict(color="green")))
fig.add_trace(go.Scatter(x=df["Mes"], y=df["Gastos"], mode="lines+markers", name="Gastos", line=dict(color="red")))

layout = html.Div([
    html.H2("Sección Finanzas", style={"textAlign": "center"}),
    dcc.Graph(figure=fig),
    html.P("Este panel muestra ingresos y gastos mensuales.")
])
