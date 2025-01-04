from dash import Dash, html, dcc, callback, Output, Input  # Importación de las librerías necesarias de Dash
import dash_table
import plotly.express as px  # Para crear gráficos interactivos
import pandas as pd  # Para la manipulación de datos con DataFrame
import gspread  # Para trabajar con Google Sheets
from oauth2client.service_account import ServiceAccountCredentials  # Para la autenticación en Google Sheets

# Configuración de credenciales para acceder a Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]  # Alcance necesario para acceder a Google Sheets y Drive
creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)  # Autenticación mediante las credenciales del archivo JSON

# Autenticación con Google
client = gspread.authorize(creds)  # Autoriza el cliente gspread para trabajar con Google Sheets

# Función para cargar los datos desde la hoja de Google Sheets
def cargar_datos():
    # Abre la hoja de Google utilizando la clave de la hoja (ID de la hoja de cálculo)
    sheet = client.open_by_key('117Zx18JKM_lk-muHBjIPqFNeTrf_LIwL5OI-Cpx2yM4').worksheet('dataset_limpio')  # Selecciona la hoja activa por su nombre
    # Extrae todos los registros de la hoja de cálculo (como lista de diccionarios)
    data = sheet.get_all_records()  # Obtiene todos los datos en un formato de lista de diccionarios
    df = pd.DataFrame(data)  # Convierte la lista de diccionarios en un DataFrame de pandas
    return df  # Retorna el DataFrame con los datos

# Inicializa el DataFrame con los datos cargados al principio
df = cargar_datos()  # Llama a la función cargar_datos para obtener los datos iniciales

# Inicializa la aplicación Dash
app = Dash()

# Obtiene las columnas del DataFrame como una lista
columnas = df.columns.tolist()  # Lista con los nombres de las columnas del DataFrame

# Define el layout (diseño) de la aplicación
app.layout = [
    html.H1(children='Title of Dash App', style={'textAlign': 'center'}),  # Título de la aplicación (centrado)
    dcc.Dropdown(  # Componente Dropdown (desplegable) para seleccionar la columna del gráfico
        id='dropdown-selection',  # ID del componente, utilizado para conectarlo con el callback
        options=[{'label': col, 'value': col} for col in columnas],  # Crea una lista de opciones para el Dropdown dinámicamente
        value=columnas[0],  # Valor por defecto, selecciona la primera columna del DataFrame
        style={'width': '50%'}  # Estilo CSS para el ancho del Dropdown
    ),
    dcc.Graph(id='graph-content'),  # Componente Graph para mostrar el gráfico generado
    dcc.Interval(  # Componente Interval para actualizar la aplicación periódicamente
        id='interval-component',  # ID del componente Interval
        interval=5*60*1000,  # Intervalo de actualización en milisegundos (5 minutos)
        n_intervals=0  # Número de intervalos que se han producido (comienza en 0)
    ),
    #Tabla de datos
    html.Div(children='Tabla de datos'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=5),
    #historgraama con el nombre de las columnas
    html.Div(children='Histograma de precio de gas natural vs precio de crudo'),
    dcc.Graph(figure=px.histogram(df, x='Natural_Gas_Price', y='Crude_oil_Price'))
]

# Callback que actualiza el gráfico en función del valor seleccionado en el Dropdown y el intervalo de tiempo
@callback(
    Output('graph-content', 'figure'),  # Salida: el contenido del gráfico (figura)
    Input('dropdown-selection', 'value'),  # Entrada: valor seleccionado en el Dropdown
    Input('interval-component', 'n_intervals')  # Entrada: número de intervalos (se activa cada vez que pasa el intervalo)
)
def update_graph(value, n_intervals):
    # Recargar los datos desde Google Sheets cada vez que se activa el callback
    df = cargar_datos()  # Llama a la función cargar_datos para obtener los datos actualizados
    # Verifica que la columna seleccionada exista en el DataFrame
    if value in df.columns:
        # Si la columna existe, crea un gráfico de línea utilizando Plotly Express
        return px.line(df, x=df.index, y=value, title=f'Gráfico de {value}')  # Crea un gráfico de línea donde 'x' es el índice del DataFrame y 'y' es la columna seleccionada
    else:
        # Si la columna no existe, retorna un gráfico vacío
        return px.line()  # Retorna un gráfico vacío si la columna seleccionada no existe

# Ejecuta la aplicación Dash
if __name__ == '__main__':  
    app.run(debug=True)  # Ejecuta el servidor de la aplicación en modo de depuración para ver los errores y actualizaciones en tiempo real
