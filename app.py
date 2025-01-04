from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np

# Crear la app Dash con estilo Bootstrap
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.FLATLY])

# Generar datos aleatorios para KPIs
np.random.seed(42)
kpis_data = pd.DataFrame({
    "Área": ["RRHH", "Finanzas", "Marketing", "Ventas", "IT", "Producción"],
    "Performance": np.random.randint(60, 100, 6),
    "Crecimiento (%)": np.random.uniform(5, 15, 6).round(2),
    "Satisfacción (%)": np.random.uniform(70, 95, 6).round(2),
    "Costos (USD)": np.random.randint(10000, 50000, 6),
})

# Gráficos de ejemplo
fig_performance = px.bar(
    kpis_data,
    x="Área",
    y="Performance",
    title="Rendimiento por Área",
    color="Área",
    text="Performance",
    labels={"Performance": "Puntaje de Rendimiento"},
    template="plotly_white",
    color_discrete_sequence=px.colors.qualitative.Pastel1
)

fig_costos = px.pie(
    kpis_data,
    names="Área",
    values="Costos (USD)",
    title="Distribución de Costos por Área",
    hole=0.4,
    template="plotly_white",
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig_crecimiento = px.line(
    kpis_data,
    x="Área",
    y="Crecimiento (%)",
    title="Crecimiento por Área",
    markers=True,
    template="plotly_white",
    line_shape="spline",
    color_discrete_sequence=px.colors.qualitative.Dark24
)

# Layout principal
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),  # Para manejar rutas
    dbc.NavbarSimple(
        brand="Empresa Dashboard",
        brand_href="/",
        color="primary",
        dark=True,
        children=[
            dbc.NavItem(dcc.Link("TH", href="th.py", className="nav-link")),
            dbc.NavItem(dcc.Link("Finances", href="finances.py", className="nav-link")),
        ],
    ),
    html.Div(id="page-content", style={"padding": "20px"}),  # Contenido dinámico
])

# Callback para cambiar el contenido según la URL
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def render_page(pathname):
    if pathname == "/":
        return html.Div([
            html.H1("Dashboard Empresarial", style={"textAlign": "center", "marginBottom": "30px"}),
            dbc.Row([
                dbc.Col(dbc.Card(
                    dbc.CardBody([
                        html.H6("Rendimiento Promedio", style={"color": "blue"}),
                        html.H4(f"{kpis_data['Performance'].mean():.2f}"),
                    ]),
                    style={"textAlign": "center", "margin": "10px"}
                ), width=3),
                dbc.Col(dbc.Card(
                    dbc.CardBody([
                        html.H6("Crecimiento Promedio", style={"color": "green"}),
                        html.H4(f"{kpis_data['Crecimiento (%)'].mean():.2f}%"),
                    ]),
                    style={"textAlign": "center", "margin": "10px"}
                ), width=3),
                dbc.Col(dbc.Card(
                    dbc.CardBody([
                        html.H6("Satisfacción Promedio", style={"color": "orange"}),
                        html.H4(f"{kpis_data['Satisfacción (%)'].mean():.2f}%"),
                    ]),
                    style={"textAlign": "center", "margin": "10px"}
                ), width=3),
            ]),
            html.Div([
                html.P("Gráfico de rendimiento por área:", style={"marginTop": "30px"}),
                dcc.Graph(figure=fig_performance),
                html.P("Distribución de costos por área:", style={"marginTop": "30px"}),
                dcc.Graph(figure=fig_costos),
                html.P("Crecimiento por área:", style={"marginTop": "30px"}),
                dcc.Graph(figure=fig_crecimiento),
            ])
        ])
    elif pathname == "/th":
        return html.Div([
            html.H2("Sección de Talento Humano", style={"textAlign": "center"}),
            html.P("Contenido relacionado con Talento Humano."),
        ])
    elif pathname == "/finances":
        return html.Div([
            html.H2("Sección de Finanzas", style={"textAlign": "center"}),
            html.P("Contenido relacionado con Finanzas."),
        ])
    return html.Div([
        html.H1("Página no encontrada", style={"textAlign": "center", "color": "red"}),
        html.P("Selecciona una sección válida desde el menú."),
    ])

if __name__ == "__main__":
    app.run_server(debug=True)
