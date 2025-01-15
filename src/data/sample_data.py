# -----------------------------------------------------------------------------
# Descripción del Código:
# Esta función genera un DataFrame de pandas con datos de ejemplo relacionados 
# con casos, resueltos y pendientes, según el mes. Los datos son fijos y 
# personalizados para cada dirección. 
#
# Información Recibida:
# - `direction`: Un parámetro que especifica la dirección de los datos, aunque
#   actualmente no afecta el contenido de los datos.
#
# Información Enviada:
# - Un DataFrame de pandas que contiene los datos de los casos para ser utilizado
#   en la aplicación, en particular para mostrar gráficos y tablas en la interfaz 
#   de usuario.
# -----------------------------------------------------------------------------

import pandas as pd  # Importa la librería pandas para manejar datos en formato de DataFrame.

def get_sample_data(direction):
    # Datos de ejemplo personalizados para cada dirección
    # La función devuelve un DataFrame con los siguientes datos fijos:
    return pd.DataFrame({
        'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May'],  # Meses de los datos
        'Casos': [120, 150, 140, 170, 190],  # Casos totales por mes
        'Resueltos': [100, 130, 120, 150, 170],  # Casos resueltos por mes
        'Pendientes': [20, 20, 20, 20, 20]  # Casos pendientes por mes
    })
