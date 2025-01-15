# -----------------------------------------------------------------------------
# Descripción del Código:
# Este código maneja los callbacks de autenticación para una aplicación Dash.
# Se definen dos callbacks:
# 1. Un callback para el inicio de sesión (login) que verifica las credenciales del usuario.
# 2. Un callback para el cierre de sesión (logout) que actualiza el estado de autenticación.
#
# Fuentes de Información:
# - El usuario proporciona las credenciales (nombre de usuario y contraseña) a través 
#   de los campos de entrada 'username' y 'password'.
# - Se compara el nombre de usuario y la contraseña con valores predefinidos (VALID_USERNAME y VALID_PASSWORD).
#
# Información Enviada:
# - El estado de autenticación actualizado (True o False) se almacena en el componente 'auth-store'.
# - En caso de error en el inicio de sesión, se muestra un mensaje de alerta con 'Credenciales incorrectas'.
#
# -----------------------------------------------------------------------------

from dash import Input, Output, State, callback, no_update  # Se importan los componentes necesarios de Dash para manejar entradas, salidas y estados.
import dash_bootstrap_components as dbc  # Se importan componentes de diseño de Bootstrap para mostrar alertas.
from config.settings import VALID_USERNAME, VALID_PASSWORD  # Se importan las credenciales válidas desde la configuración.

def register_auth_callbacks(app):  # Función que registra los callbacks de autenticación en la aplicación Dash.
    # Callback para el inicio de sesión (login)
    @callback(
        [Output('auth-store', 'data'),  # Se actualiza el estado de autenticación en 'auth-store'.
         Output('login-output', 'children')],  # Se muestra un mensaje si las credenciales son incorrectas.
        [Input('login-button', 'n_clicks')],  # Input: clic en el botón de login.
        [State('username', 'value'),  # Estado: valor del campo de nombre de usuario.
         State('password', 'value')],  # Estado: valor del campo de contraseña.
        prevent_initial_call=True  # Evita que el callback se dispare al inicio sin interacción del usuario.
    )
    def login(n_clicks, username, password):  # Función que maneja el proceso de inicio de sesión.
        if not n_clicks:  # Si no ha habido clics en el botón de login, no se hace ninguna actualización.
            return no_update, no_update
        if username == VALID_USERNAME and password == VALID_PASSWORD:  # Verificación de credenciales.
            return {'authenticated': True}, None  # Si las credenciales son correctas, se marca como autenticado.
        return {'authenticated': False}, dbc.Alert('Credenciales incorrectas', color='danger')  # Si son incorrectas, se muestra una alerta.

    # Callback para el cierre de sesión (logout)
    @callback(
        Output('auth-store', 'data', allow_duplicate=True),  # Se actualiza el estado de autenticación en 'auth-store'.
        Input('logout-button', 'n_clicks'),  # Input: clic en el botón de logout.
        prevent_initial_call=True  # Evita que el callback se dispare al inicio sin interacción del usuario.
    )
    def logout(n_clicks):  # Función que maneja el proceso de cierre de sesión.
        if n_clicks:  # Si el botón de logout ha sido presionado.
            return {'authenticated': False}  # Se actualiza el estado de autenticación a 'False' (desconectado).
        return no_update  # Si no se ha hecho clic, no se actualiza nada.
