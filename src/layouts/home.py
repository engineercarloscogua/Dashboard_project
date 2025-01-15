# -----------------------------------------------------------------------------
# Descripción del Código:
# Este código define una función que crea el contenido principal de la página de inicio 
# de la aplicación Dash. La interfaz está compuesta por un contenedor con tres columnas,
# cada una mostrando una tarjeta con un ícono, un título y una breve descripción.
# Cada tarjeta representa un área clave de la EPS (Entidad Promotora de Salud).
#
# Fuentes de Información:
# - El contenido es estático, basado en los títulos y descripciones predefinidos.
# - Utiliza componentes de Dash Bootstrap para crear la estructura visual.
#
# Información Enviada:
# - Se envía un layout con tres tarjetas que se muestran en la página principal.
# - Cada tarjeta está enfocada en una sección específica (Indicadores Generales, Gestión de Usuarios, Procesos).
#
# -----------------------------------------------------------------------------

import dash_bootstrap_components as dbc  # Se importa Dash Bootstrap Components para crear componentes visuales con Bootstrap.
from dash import html  # Se importa el módulo html de Dash para construir los elementos HTML.

def create_home_content():
    # Se crea un contenedor (Container) que alberga una fila (Row) de tres columnas (Col).
    return dbc.Container([
        dbc.Row([  # Se define una fila que contendrá las tres columnas.
            dbc.Col([  # Primera columna con el contenido de "Indicadores Generales".
                dbc.Card([  # Se crea una tarjeta (Card) para mostrar información.
                    dbc.CardBody([  # Cuerpo de la tarjeta donde se coloca el contenido.
                        html.I(className="fas fa-chart-line fa-3x text-primary mb-3"),  # Ícono de gráfico de líneas (indicadores).
                        html.H4("Indicadores Generales", className="card-title"),  # Título de la tarjeta.
                        html.P("Visualización de métricas clave de la EPS")  # Descripción de la tarjeta.
                    ], className="text-center")  # Centramos el contenido dentro de la tarjeta.
                ], className="mb-4 shadow-sm")  # Margen inferior y sombra suave para la tarjeta.
            ], md=4),  # La columna ocupa 4 de 12 unidades del ancho de la pantalla.
            dbc.Col([  # Segunda columna con el contenido de "Gestión de Usuarios".
                dbc.Card([  # Se crea una tarjeta similar a la anterior.
                    dbc.CardBody([  # Cuerpo de la tarjeta.
                        html.I(className="fas fa-users fa-3x text-success mb-3"),  # Ícono de usuarios.
                        html.H4("Gestión de Usuarios", className="card-title"),  # Título de la tarjeta.
                        html.P("Información sobre afiliados y servicios")  # Descripción de la tarjeta.
                    ], className="text-center")  # Centramos el contenido dentro de la tarjeta.
                ], className="mb-4 shadow-sm")  # Margen inferior y sombra suave para la tarjeta.
            ], md=4),  # La columna ocupa 4 de 12 unidades del ancho de la pantalla.
            dbc.Col([  # Tercera columna con el contenido de "Procesos".
                dbc.Card([  # Se crea una tarjeta similar a las anteriores.
                    dbc.CardBody([  # Cuerpo de la tarjeta.
                        html.I(className="fas fa-tasks fa-3x text-info mb-3"),  # Ícono de tareas.
                        html.H4("Procesos", className="card-title"),  # Título de la tarjeta.
                        html.P("Estado de procesos y trámites")  # Descripción de la tarjeta.
                    ], className="text-center")  # Centramos el contenido dentro de la tarjeta.
                ], className="mb-4 shadow-sm")  # Margen inferior y sombra suave para la tarjeta.
            ], md=4),  # La columna ocupa 4 de 12 unidades del ancho de la pantalla.
        ])
    ])
