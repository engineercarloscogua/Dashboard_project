# -----------------------------------------------------------------------------
# Descripción del Código:
# Este código define una función llamada `create_direction_content`, la cual genera 
# el contenido para una página de un área o dirección específica. La función crea 
# dos gráficos interactivos con Plotly: un gráfico de líneas con área que muestra 
# los casos mensuales, y un gráfico de barras apiladas que muestra el estado de los 
# casos (resueltos y pendientes). Además, se presenta una tabla con indicadores de gestión.
#
# Fuentes de Información:
# - Los datos para los gráficos se obtienen a través de la función `get_sample_data` 
#   de `src.data.sample_data`, que toma un parámetro `direction`.
# - Los gráficos se generan usando la biblioteca Plotly.
# 
# Información Enviada:
# - La función devuelve un layout con los gráficos generados y una tabla con los datos.
#
# Información Recibida:
# - Recibe dos parámetros: `direction`, que especifica la dirección (o área) a visualizar,
#   y `title`, que es el título de la página que se muestra.
# -----------------------------------------------------------------------------

import dash_bootstrap_components as dbc  # Se importa Dash Bootstrap Components para crear componentes con Bootstrap.
from dash import html, dcc  # Se importan componentes HTML y gráficos de Dash.
import plotly.graph_objects as go  # Se importa Plotly para crear gráficos.
from src.data.sample_data import get_sample_data  # Se importa la función para obtener los datos de ejemplo.

def create_direction_content(direction, title):
    # Obtención de los datos de ejemplo para la dirección especificada.
    df = get_sample_data(direction)
    
    # Gráfico de líneas con área que muestra los casos mensuales.
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=df['Mes'],  # Meses en el eje X.
        y=df['Casos'],  # Casos totales en el eje Y.
        fill='tonexty',  # Relleno debajo de la línea.
        name='Casos Totales',  # Nombre de la serie.
        line=dict(color='#18BC9C')  # Color de la línea.
    ))
    fig1.update_layout(
        title=f'Casos Mensuales - {title}',  # Título dinámico con el nombre de la dirección.
        template='plotly_white',  # Plantilla de gráfico blanco.
        height=400,  # Altura del gráfico.
        margin=dict(l=40, r=40, t=40, b=40)  # Márgenes del gráfico.
    )

    # Gráfico de barras apiladas mostrando el estado de los casos (resueltos y pendientes).
    fig2 = go.Figure(data=[
        go.Bar(name='Resueltos', x=df['Mes'], y=df['Resueltos'], marker_color='#2C3E50'),  # Casos resueltos.
        go.Bar(name='Pendientes', x=df['Mes'], y=df['Pendientes'], marker_color='#E74C3C')  # Casos pendientes.
    ])
    fig2.update_layout(
        barmode='stack',  # Apilar las barras.
        title='Estado de Casos',  # Título del gráfico.
        template='plotly_white',  # Plantilla de gráfico blanco.
        height=400,  # Altura del gráfico.
        margin=dict(l=40, r=40, t=40, b=40)  # Márgenes del gráfico.
    )

    # Creación del layout con los gráficos y la tabla.
    return dbc.Container([
        dbc.Row([  # Se define una fila para colocar los elementos.
            dbc.Col([  # Columna principal que contiene los gráficos y la tabla.
                html.H2(title, className="text-center mb-4"),  # Título de la página, centrado.
                dbc.Row([  # Fila para los gráficos.
                    dbc.Col(  # Columna para el primer gráfico.
                        dbc.Card([  # Tarjeta para contener el gráfico.
                            dbc.CardBody([  # Cuerpo de la tarjeta.
                                dcc.Graph(figure=fig1)  # Gráfico de líneas.
                            ])
                        ], className="shadow-sm mb-4"),  # Clase de tarjeta con sombra y margen inferior.
                        md=6  # Columna de tamaño medio.
                    ),
                    dbc.Col(  # Columna para el segundo gráfico.
                        dbc.Card([  # Tarjeta para contener el gráfico.
                            dbc.CardBody([  # Cuerpo de la tarjeta.
                                dcc.Graph(figure=fig2)  # Gráfico de barras apiladas.
                            ])
                        ], className="shadow-sm mb-4"),  # Clase de tarjeta con sombra y margen inferior.
                        md=6  # Columna de tamaño medio.
                    ),
                ]),
                dbc.Row([  # Fila para la tabla de indicadores.
                    dbc.Col(  # Columna para la tabla.
                        dbc.Card([  # Tarjeta para contener la tabla.
                            dbc.CardHeader(html.H5("Indicadores de Gestión")),  # Encabezado de la tarjeta.
                            dbc.CardBody([  # Cuerpo de la tarjeta.
                                dbc.Table.from_dataframe(  # Creación de la tabla a partir del DataFrame.
                                    df,
                                    striped=True,  # Filas con rayas.
                                    bordered=True,  # Bordes en la tabla.
                                    hover=True,  # Resaltado de las filas al pasar el ratón.
                                    responsive=True,  # Tabla adaptativa al tamaño de pantalla.
                                    className="mb-0"  # Clase de margen para la tabla.
                                )
                            ])
                        ], className="shadow-sm"),  # Tarjeta con sombra.
                        md=12  # Columna de tamaño completo.
                    )
                ])
            ])
        ])
    ])
