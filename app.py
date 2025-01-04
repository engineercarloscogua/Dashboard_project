# Importamos las librerías necesarias para crear la app Dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import random

# Creamos la aplicación Dash, con estilo Bootstrap (que hace que la app se vea más profesional)
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.FLATLY])

# Definimos una paleta de colores pastel para los gráficos (esto hace que se vean suaves y agradables)
pastel_colors = ['#f4c7c3', '#f7d7b3', '#f3e3d4', '#e0c9f0', '#d1f0e1', '#f9e0a1']

# Función para generar datos aleatorios para cada área de la empresa
def generar_datos_area(area, periodo):
    # Definimos qué indicadores medir en cada área
    categorias = {
        'Ventas': ['Ingresos', 'Crecimiento', 'Nuevos Clientes', 'Satisfacción'],
        'Finanzas': ['Rentabilidad', 'Deuda', 'Eficiencia', 'ROI'],
        'Recursos Humanos': ['Retención', 'Contratación', 'Capacitación', 'Satisfacción Empleados'],
        'Producción': ['Producción Total', 'Eficiencia', 'Costos', 'Tiempo de Inactividad'],
        'Marketing': ['Alcance', 'Conversiones', 'Tráfico Web', 'Retorno de Inversión'],
        'Atención al Cliente': ['Satisfacción', 'Tiempo de Respuesta', 'Respuestas Resueltas', 'Feedback']
    }

    # Generamos valores aleatorios (de 50 a 100) para los indicadores
    valores = [random.randint(50, 100) for _ in range(4)]  # 4 indicadores por área
    return categorias[area], valores  # Retorna los nombres de los indicadores y sus valores

# Función para crear un gráfico de barras (como los gráficos tradicionales)
def crear_grafico_barras(area, periodo):
    categorias, valores = generar_datos_area(area, periodo)
    return dcc.Graph(
        id=f'grafico-barras-{area}',  # Cada gráfico tiene un ID único
        figure={
            'data': [
                go.Bar(
                    x=categorias,  # Los indicadores en el eje X
                    y=valores,  # Los valores de los indicadores en el eje Y
                    name=f'{area} - {periodo}',  # Título del gráfico
                    marker=dict(color=pastel_colors[:len(categorias)])  # Colores pastel
                )
            ],
            'layout': go.Layout(
                title=f'Indicadores de Gestión: {area} ({periodo})',  # Título del gráfico
                xaxis={'title': 'Indicadores'},  # Título del eje X
                yaxis={'title': 'Valor'},  # Título del eje Y
                template='plotly',  # Estilo visual de los gráficos
                height=400  # Altura del gráfico
            )
        }
    )

# Función para crear un gráfico de líneas (para mostrar tendencias a lo largo del tiempo)
def crear_grafico_lineas(area, periodo):
    categorias, valores = generar_datos_area(area, periodo)
    return dcc.Graph(
        id=f'grafico-lineas-{area}',
        figure={
            'data': [
                go.Scatter(
                    x=categorias,  # Los indicadores en el eje X
                    y=valores,  # Los valores de los indicadores en el eje Y
                    mode='lines+markers',  # Modo de gráfico de líneas con puntos
                    name=f'{area} - {periodo}',  # Título del gráfico
                    marker=dict(color=pastel_colors[:len(categorias)])  # Colores pastel
                )
            ],
            'layout': go.Layout(
                title=f'Tendencia de Gestión: {area} ({periodo})',  # Título del gráfico
                xaxis={'title': 'Indicadores'},  # Título del eje X
                yaxis={'title': 'Valor'},  # Título del eje Y
                template='plotly',  # Estilo visual de los gráficos
                height=400  # Altura del gráfico
            )
        }
    )

# Función para crear un gráfico circular (pie chart), ideal para mostrar proporciones
def crear_grafico_pie(area, periodo):
    categorias, valores = generar_datos_area(area, periodo)
    return dcc.Graph(
        id=f'grafico-pie-{area}',
        figure={
            'data': [
                go.Pie(
                    labels=categorias,  # Los indicadores como etiquetas
                    values=valores,  # Los valores de cada indicador
                    name=f'{area} - {periodo}',  # Título del gráfico
                    marker=dict(colors=pastel_colors[:len(categorias)])  # Colores pastel
                )
            ],
            'layout': go.Layout(
                title=f'Distribución de Indicadores: {area} ({periodo})',  # Título del gráfico
                template='plotly',  # Estilo visual de los gráficos
                height=400  # Altura del gráfico
            )
        }
    )

# Layout principal de la aplicación (lo que verá el usuario)
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),  # Para manejar rutas dentro de la app
    dbc.NavbarSimple(
        brand="Empresa Dashboard",  # Nombre del dashboard
        brand_href="/",  # Enlace al inicio
        color="primary",  # Color del navbar
        dark=True,  # Estilo oscuro
        children=[
            dbc.NavItem(dcc.Link("TH", href="/th", className="nav-link")),  # Enlace a la sección de Recursos Humanos
            dbc.NavItem(dcc.Link("Finances", href="/finances", className="nav-link")),  # Enlace a la sección de Finanzas
        ],
    ),
    html.Div(id="page-content", style={"padding": "20px"}),  # Área donde se cambia el contenido según la ruta
])

# Callback que maneja las rutas de la app y carga el contenido según la URL
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")  # Escucha el cambio en la URL
)
def render_page(pathname):
    if pathname == "/th":
        from pages.th import layout as th_layout  # Cargar la página de Recursos Humanos
        return th_layout
    elif pathname == "/finances":
        from pages.finances import layout as finances_layout  # Cargar la página de Finanzas
        return finances_layout
    
    # Página principal con gráficos
    return html.Div([
        html.H1("Bienvenido al Dashboard Empresarial", style={"textAlign": "center"}),  # Título de la página
        html.P("Selecciona una sección para continuar.", style={"textAlign": "center"}),  # Mensaje introductorio
        html.Br(),
        
        # Filtros para seleccionar el área y el periodo de tiempo
        html.Div([
            dbc.Row([
                dbc.Col(dcc.Dropdown(
                    id='area-dropdown',  # Dropdown para seleccionar el área de la empresa
                    options=[
                        {'label': 'Ventas', 'value': 'Ventas'},
                        {'label': 'Finanzas', 'value': 'Finanzas'},
                        {'label': 'Recursos Humanos', 'value': 'Recursos Humanos'},
                        {'label': 'Producción', 'value': 'Producción'},
                        {'label': 'Marketing', 'value': 'Marketing'},
                        {'label': 'Atención al Cliente', 'value': 'Atención al Cliente'},
                    ],
                    value='Ventas',  # Valor inicial seleccionado
                    style={'width': '50%'}
                )),
                
                dbc.Col(dcc.Dropdown(
                    id='periodo-dropdown',  # Dropdown para seleccionar el periodo (Semanal, Mensual, etc.)
                    options=[
                        {'label': 'Semanal', 'value': 'Semanal'},
                        {'label': 'Mensual', 'value': 'Mensual'},
                        {'label': 'Trimestral', 'value': 'Trimestral'},
                        {'label': 'Semestral', 'value': 'Semestral'},
                        {'label': 'Anual', 'value': 'Anual'},
                    ],
                    value='Mensual',  # Valor inicial seleccionado
                    style={'width': '50%'}
                )),
            ])
        ], style={'marginBottom': '20px'}),

        # Área donde se mostrarán los gráficos de las áreas seleccionadas
        html.Div(id="grafico-area", children=[
            crear_grafico_barras('Ventas', 'Mensual'),
            crear_grafico_lineas('Ventas', 'Mensual'),
            crear_grafico_pie('Ventas', 'Mensual'),
        ])
    ])

# Callback para actualizar los gráficos cuando el usuario cambia el área o el periodo
@app.callback(
    Output("grafico-area", "children"),
    [Input("area-dropdown", "value"),  # Escucha el cambio de área
     Input("periodo-dropdown", "value")]  # Escucha el cambio de periodo
)
def update_grafico(area, periodo):
    # Devuelve los gráficos actualizados según la selección
    return [
        crear_grafico_barras(area, periodo),
        crear_grafico_lineas(area, periodo),
        crear_grafico_pie(area, periodo),
    ]

# Finalmente, ejecutamos la app
if __name__ == "__main__":
    app.run_server(debug=True)
