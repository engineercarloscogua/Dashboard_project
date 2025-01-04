from dash import html, dcc
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Datos ficticios para la gráfica
np.random.seed(42)
df = pd.DataFrame({
    "Departamento": ["RRHH", "IT", "Ventas", "Marketing"],
    "Performance": np.random.randint(50, 100, 4)
})

# Gráfica de barras
fig = go.Figure(data=[
    go.Bar(x=df["Departamento"], y=df["Performance"], name="Performance", marker_color="blue")
])

# Layout con un diseño de grid y dropdown
layout = html.Div([
    # Título general
    html.H2("Sección Talento Humano", style={"textAlign": "center", "padding": "10px", "backgroundColor": "#2c3e50", "color": "white"}),

    # Dropdown para selección única
    html.Div([
        html.Label("Seleccione una categoría:", style={"fontWeight": "bold", "fontSize": "16px", "color": "#2c3e50"}),
        dcc.Dropdown(
            id="category-dropdown",
            options=[
                {"label": "Rotación de Personal", "value": "rotacion"},
                {"label": "Capacitación", "value": "capacitacion"},
                {"label": "Incentivos", "value": "incentivos"},
                {"label": "Evaluación", "value": "evaluacion"},
                {"label": "Bienestar", "value": "bienestar"},
                {"label": "Clima Organizacional", "value": "clima"},
                {"label": "Retención de Talento", "value": "retencion"}
            ],
            placeholder="Seleccione una categoría",
            style={"width": "50%", "marginBottom": "20px"}
        )
    ], style={"padding": "15px"}),

    # Contenedor de tres secciones
    html.Div([
        # Primera sección: Análisis Descriptivo
        html.Div([
            html.H4("Análisis Descriptivo", style={"textAlign": "center", "color": "#2c3e50"}),
            html.P("En esta sección se detalla el análisis descriptivo de los datos.", style={"textAlign": "justify"}),
        ], style={"border": "1px solid #2c3e50", "borderRadius": "5px", "padding": "15px", "backgroundColor": "#ecf0f1"}),

        # Segunda sección: Diagnóstico
        html.Div([
            html.H4("Diagnóstico", style={"textAlign": "center", "color": "#2c3e50"}),
            html.P("Aquí se encuentra el diagnóstico basado en los datos disponibles.", style={"textAlign": "justify"}),
        ], style={"border": "1px solid #2c3e50", "borderRadius": "5px", "padding": "15px", "backgroundColor": "#ecf0f1"}),

        # Tercera sección: Predictivo
        html.Div([
            html.H4("Predictivo", style={"textAlign": "center", "color": "#2c3e50"}),
            html.P("Predicciones y proyecciones basadas en modelos de datos.", style={"textAlign": "justify"}),
        ], style={"border": "1px solid #2c3e50", "borderRadius": "5px", "padding": "15px", "backgroundColor": "#ecf0f1"}),
    ], style={
        "display": "grid",
        "gridTemplateColumns": "1fr 1fr 1fr",
        "gap": "15px",
        "padding": "20px"
    }),

    # Gráfica de barras
    html.Div([
        dcc.Graph(figure=fig)
    ], style={"padding": "20px"})
])
