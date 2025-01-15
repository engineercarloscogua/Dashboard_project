# -----------------------------------------------------------------------------
# Descripción del Código:
# Este código configura una aplicación web utilizando Dash. La aplicación gestiona
# la navegación de las páginas y la autenticación de los usuarios. Se inicia
# la aplicación, se establece la estructura básica del layout, y se implementa 
# un callback que cambia el contenido de la página dependiendo de la URL actual 
# y el estado de autenticación del usuario.
#
# Fuentes de Información:
# - La URL de la página se maneja a través del componente dcc.Location.
# - El estado de autenticación se maneja a través de dcc.Store y se utiliza 
#   en los callbacks para determinar si mostrar el contenido de la página o 
#   la tarjeta de inicio de sesión.
#
# Información Enviada:
# - Se envía el contenido de la página actualizado a la interfaz de usuario 
#   a través del componente 'page-content'.
#
# -----------------------------------------------------------------------------

from dash import Dash, html, dcc, Input, Output  # Se importan los componentes esenciales de Dash, incluyendo Input y Output que se usan para crear interactividad.
import dash_bootstrap_components as dbc  # Se importan los componentes de diseño de Bootstrap para mejorar la apariencia.
from config.settings import EXTERNAL_STYLESHEETS, COLORS  # Se importan configuraciones externas, como hojas de estilo y colores definidos.
from src.components.navbar import create_navbar  # Se importa la función para crear la barra de navegación.
from src.components.login import create_login_card  # Se importa la función para crear la tarjeta de inicio de sesión.
from src.layouts.home import create_home_content  # Se importa la función para crear el contenido principal de la página de inicio.
from src.layouts.direction import create_direction_content  # Se importa la función para crear el contenido de las distintas direcciones.
from src.auth import register_auth_callbacks  # Se importa la función para registrar los callbacks de autenticación.

# Inicialización de la aplicación Dash
app = Dash(
    __name__,  # El nombre del módulo para la app.
    external_stylesheets=EXTERNAL_STYLESHEETS,  # Se configuran las hojas de estilo externas desde el archivo de configuración.
    suppress_callback_exceptions=True  # Se permite que existan callbacks sin excepciones hasta ser registrados.
)

# Creación del layout de la aplicación, es decir, la estructura de la interfaz de usuario.
app.layout = html.Div([  # Se crea un contenedor principal con una estructura HTML.
    dcc.Location(id='url', refresh=False),  # Componente para manejar la URL y determinar la página actual.
    dcc.Store(id='auth-store', data={'authenticated': False}),  # Componente para almacenar el estado de autenticación.
    html.Div(id='page-content')  # Componente donde se renderizará el contenido de la página según la ruta.
], style={'backgroundColor': COLORS['background'], 'minHeight': '100vh'})  # Estilos para el fondo y altura mínima.

# Registro de los callbacks relacionados con la autenticación
register_auth_callbacks(app)  # Se registra la función para manejar la autenticación de los usuarios.

# Callback para cambiar el contenido de la página según la URL y el estado de autenticación.
@app.callback(
    Output('page-content', 'children'),  # El contenido de la página será actualizado en 'page-content'.
    [Input('url', 'pathname'),  # El input es la URL actual.
     Input('auth-store', 'data')]  # El input es también el estado de autenticación.
)
def display_page(pathname, auth_data):  # Función que actualiza la página según la ruta y el estado de autenticación.
    authenticated = auth_data.get('authenticated', False) if auth_data else False  # Se obtiene el estado de autenticación.
    
    # Si no está autenticado, se muestra la tarjeta de inicio de sesión.
    if not authenticated:
        return dbc.Container(
            dbc.Row(
                dbc.Col(create_login_card(), md=6, lg=4),  # Se crea la tarjeta de login en una columna centrada.
                justify="center",  # Justifica la columna al centro.
                align="center",  # Alinea el contenido al centro.
                style={"minHeight": "100vh"}  # Se asegura de que la altura mínima sea completa en la pantalla.
            )
        )
    
    # Si está autenticado, se genera el contenido de la página según la ruta.
    content = html.Div([  # Se crea un contenedor para el contenido.
        create_navbar(),  # Se incluye la barra de navegación.
        html.Div([  # Se genera el contenido según la URL.
            create_home_content() if pathname == '/' else  # Página de inicio.
            create_direction_content('juridica', 'Oficina Asesora Jurídica') if pathname == '/juridica' else  # Oficina Jurídica.
            create_direction_content('control', 'Oficina de Control Interno') if pathname == '/control-interno' else  # Oficina de Control Interno.
            create_direction_content('administrativa', 'Dirección Administrativa y Financiera') if pathname == '/administrativa' else  # Dirección Administrativa.
            create_direction_content('salud', 'Dirección de Salud Pública') if pathname == '/salud-publica' else  # Dirección de Salud Pública.
            create_direction_content('seguridad', 'Dirección de Seguridad Social') if pathname == '/seguridad-social' else  # Dirección de Seguridad Social.
            create_direction_content('aseguramiento', 'Dirección de Aseguramiento') if pathname == '/aseguramiento' else  # Dirección de Aseguramiento.
            create_home_content()  # Si no se encuentra una ruta válida, se muestra la página de inicio.
        ], className="mt-4 mb-4")  # Se aplica margen superior e inferior al contenido.
    ])
    
    return content  # Se devuelve el contenido generado según la ruta y el estado de autenticación.
