# ============================
# Componente de Tarjeta de Inicio de Sesión
# ============================

import dash_bootstrap_components as dbc  # Importa los componentes de Bootstrap para Dash
from dash import html  # Importa los componentes HTML de Dash

# Función para crear la tarjeta de inicio de sesión
def create_login_card():
    return dbc.Card([
        dbc.CardBody([
            html.Div([
                html.I(className="fas fa-hospital-user fa-3x text-primary mb-3"),  # Ícono de usuario con estilo
                html.H2("Dashboard EPS", className="text-center mb-4"),  # Título centrado del dashboard
                
                # Campo de entrada para el nombre de usuario
                dbc.Input(
                    id="username",  # ID del input para el usuario
                    placeholder="Usuario",  # Texto de ayuda
                    type="text",  # Tipo de dato: texto
                    className="mb-3",  # Margen inferior
                    style={"borderRadius": "10px"}  # Bordes redondeados
                ),
                
                # Campo de entrada para la contraseña
                dbc.Input(
                    id="password",  # ID del input para la contraseña
                    placeholder="Contraseña",  # Texto de ayuda
                    type="password",  # Tipo de dato: contraseña
                    className="mb-3",  # Margen inferior
                    style={"borderRadius": "10px"}  # Bordes redondeados
                ),
                
                # Botón para iniciar sesión
                dbc.Button(
                    "Iniciar Sesión",  # Texto del botón
                    id="login-button",  # ID del botón
                    color="primary",  # Color primario
                    className="w-100",  # Ocupa el ancho completo
                    style={"borderRadius": "10px"}  # Bordes redondeados
                ),
                
                # Espacio para mostrar mensajes de inicio de sesión
                html.Div(id="login-output", className="mt-3")  # Div para mostrar mensajes debajo del botón
            ], className="text-center")  # Centra todo el contenido de la tarjeta
        ])
    ], className="shadow", style={"borderRadius": "15px"})  # Agrega sombra y bordes redondeados a la tarjeta
