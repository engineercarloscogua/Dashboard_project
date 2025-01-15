# Este módulo configura las variables de entorno, las credenciales de acceso y los estilos visuales para una aplicación Dash.
# Se comunica con un archivo .env para obtener las credenciales y aplica estilos con hojas de estilo externas.
# Los datos de usuario y contraseña se utilizan para validar el acceso a la aplicación.

import os  # Importa el módulo 'os' para interactuar con el sistema operativo
from dotenv import load_dotenv  # Importa la función 'load_dotenv' para cargar variables de entorno desde un archivo .env

# Cargar las variables de entorno desde un archivo .env
load_dotenv()

# Credenciales de acceso obtenidas desde las variables de entorno, con valores predeterminados si no se encuentran definidas
VALID_USERNAME = os.getenv('VALID_USERNAME', 'lumethik')  # Usuario válido, por defecto 'lumethik'
VALID_PASSWORD = os.getenv('VALID_PASSWORD', '2025')  # Contraseña válida, por defecto '2025'

# Paleta de colores utilizada en la aplicación
COLORS = {
    'primary': '#2C3E50',  # Color principal (azul oscuro)
    'secondary': '#18BC9C',  # Color secundario (verde)
    'background': '#ECF0F1',  # Color de fondo (gris claro)
    'text': '#2C3E50'  # Color del texto (azul oscuro)
}

# Hojas de estilo externas para el diseño de la aplicación
EXTERNAL_STYLESHEETS = [
    'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css',  # Hoja de estilo de Bootstrap 5 para componentes responsivos
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css'  # Íconos de Font Awesome 6
]
