# -----------------------------------------------------------------------------
# Descripción del Código:
# Este código es el punto de entrada para ejecutar la aplicación Dash. Importa 
# la instancia de la aplicación desde `src.app` y ejecuta el servidor de Dash 
# cuando el script se ejecuta directamente. Se establece el modo de depuración 
# (`debug=True`) para facilitar la detección de errores y mejorar el desarrollo.
# 
# Información Enviada:
# - La aplicación Dash se ejecuta en el servidor, permitiendo visualizar la interfaz 
#   de usuario en el navegador.
#
# Información Recibida:
# - La instancia de la aplicación Dash `app` se importa desde `src.app`.
# -----------------------------------------------------------------------------

from src.app import app  # Importa la instancia de la aplicación Dash.

if __name__ == '__main__':  # Verifica si el script se ejecuta directamente.
    app.run_server(debug=True)  # Inicia el servidor de la aplicación Dash en modo depuración.
