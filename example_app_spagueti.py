from dash import Dash, dcc, html, Input, Output, State, callback, no_update
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración inicial con tema claro y profesional
app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.FLATLY,  # Tema más profesional
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
    ]
)

# Credenciales
VALID_USERNAME = 'lumethik'
VALID_PASSWORD = '2025'

# Colores corporativos
COLORS = {
    'primary': '#2C3E50',
    'secondary': '#18BC9C',
    'background': '#ECF0F1',
    'text': '#2C3E50'
}

# Componente de login mejorado
login_card = dbc.Card([
    dbc.CardBody([
        html.Div([
            html.I(className="fas fa-hospital-user fa-3x text-primary mb-3"),
            html.H2("Dashboard EPS", className="text-center mb-4"),
            dbc.Input(
                id="username",
                placeholder="Usuario",
                type="text",
                className="mb-3",
                style={"borderRadius": "10px"}
            ),
            dbc.Input(
                id="password",
                placeholder="Contraseña",
                type="password",
                className="mb-3",
                style={"borderRadius": "10px"}
            ),
            dbc.Button(
                "Iniciar Sesión",
                id="login-button",
                color="primary",
                className="w-100",
                style={"borderRadius": "10px"}
            ),
            html.Div(id="login-output", className="mt-3")
        ], className="text-center")
    ])
], className="shadow", style={"borderRadius": "15px"})

# Barra de navegación mejorada
navbar = dbc.NavbarSimple(
    children=[
        dbc.Nav([
            dbc.NavItem(dbc.NavLink("Inicio", href="/", className="px-3")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Oficina Asesora Jurídica", href="/juridica"),
                    dbc.DropdownMenuItem("Oficina de Control Interno", href="/control-interno"),
                    dbc.DropdownMenuItem("Dirección Administrativa y Financiera", href="/administrativa"),
                    dbc.DropdownMenuItem("Dirección de Salud Pública", href="/salud-publica"),
                    dbc.DropdownMenuItem("Dirección de Seguridad Social", href="/seguridad-social"),
                    dbc.DropdownMenuItem("Dirección de Aseguramiento", href="/aseguramiento"),
                ],
                nav=True,
                label="Direcciones",
                className="px-3",
            ),
            dbc.NavItem(dbc.Button("Cerrar Sesión", id="logout-button", color="danger", size="sm", className="ms-2")),
        ], navbar=True)
    ],
    brand="Dashboard EPS",
    brand_href="/",
    color="primary",
    dark=True,
    className="mb-4",
)

# Funciones para generar contenido
def get_sample_data(direction):
    # Datos de ejemplo personalizados para cada dirección
    return pd.DataFrame({
        'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May'],
        'Casos': [120, 150, 140, 170, 190],
        'Resueltos': [100, 130, 120, 150, 170],
        'Pendientes': [20, 20, 20, 20, 20]
    })

def create_home_content():
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.I(className="fas fa-chart-line fa-3x text-primary mb-3"),
                        html.H4("Indicadores Generales", className="card-title"),
                        html.P("Visualización de métricas clave de la EPS")
                    ], className="text-center")
                ], className="mb-4 shadow-sm")
            ], md=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.I(className="fas fa-users fa-3x text-success mb-3"),
                        html.H4("Gestión de Usuarios", className="card-title"),
                        html.P("Información sobre afiliados y servicios")
                    ], className="text-center")
                ], className="mb-4 shadow-sm")
            ], md=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.I(className="fas fa-tasks fa-3x text-info mb-3"),
                        html.H4("Procesos", className="card-title"),
                        html.P("Estado de procesos y trámites")
                    ], className="text-center")
                ], className="mb-4 shadow-sm")
            ], md=4),
        ])
    ])

def create_direction_content(direction, title):
    df = get_sample_data(direction)
    
    # Gráfico de líneas con área
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=df['Mes'],
        y=df['Casos'],
        fill='tonexty',
        name='Casos Totales',
        line=dict(color='#18BC9C')
    ))
    fig1.update_layout(
        title=f'Casos Mensuales - {title}',
        template='plotly_white',
        height=400,
        margin=dict(l=40, r=40, t=40, b=40)
    )

    # Gráfico de barras apiladas
    fig2 = go.Figure(data=[
        go.Bar(name='Resueltos', x=df['Mes'], y=df['Resueltos'], marker_color='#2C3E50'),
        go.Bar(name='Pendientes', x=df['Mes'], y=df['Pendientes'], marker_color='#E74C3C')
    ])
    fig2.update_layout(
        barmode='stack',
        title='Estado de Casos',
        template='plotly_white',
        height=400,
        margin=dict(l=40, r=40, t=40, b=40)
    )

    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H2(title, className="text-center mb-4"),
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardBody([
                                dcc.Graph(figure=fig1)
                            ])
                        ], className="shadow-sm mb-4"),
                        md=6
                    ),
                    dbc.Col(
                        dbc.Card([
                            dbc.CardBody([
                                dcc.Graph(figure=fig2)
                            ])
                        ], className="shadow-sm mb-4"),
                        md=6
                    ),
                ]),
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader(html.H5("Indicadores de Gestión")),
                            dbc.CardBody([
                                dbc.Table.from_dataframe(
                                    df,
                                    striped=True,
                                    bordered=True,
                                    hover=True,
                                    responsive=True,
                                    className="mb-0"
                                )
                            ])
                        ], className="shadow-sm"),
                        md=12
                    )
                ])
            ])
        ])
    ])

# Layout principal
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='auth-store', data={'authenticated': False}),
    html.Div(id='page-content')
], style={'backgroundColor': COLORS['background'], 'minHeight': '100vh'})

# Callbacks
@callback(
    [Output('auth-store', 'data'),
     Output('login-output', 'children')],
    [Input('login-button', 'n_clicks')],
    [State('username', 'value'),
     State('password', 'value')],
    prevent_initial_call=True
)
def login(n_clicks, username, password):
    if not n_clicks:
        return no_update, no_update
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return {'authenticated': True}, None
    return {'authenticated': False}, dbc.Alert('Credenciales incorrectas', color='danger')

@callback(
    Output('auth-store', 'data', allow_duplicate=True),
    Input('logout-button', 'n_clicks'),
    prevent_initial_call=True
)
def logout(n_clicks):
    if n_clicks:
        return {'authenticated': False}
    return no_update

@callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname'),
     Input('auth-store', 'data')]
)
def display_page(pathname, auth_data):
    authenticated = auth_data.get('authenticated', False) if auth_data else False
    
    if not authenticated:
        return dbc.Container(
            dbc.Row(
                dbc.Col(login_card, md=6, lg=4),
                justify="center",
                align="center",
                style={"minHeight": "100vh"}
            )
        )
    
    content = html.Div([
        navbar,
        html.Div([
            create_home_content() if pathname == '/' else
            create_direction_content('juridica', 'Oficina Asesora Jurídica') if pathname == '/juridica' else
            create_direction_content('control', 'Oficina de Control Interno') if pathname == '/control-interno' else
            create_direction_content('administrativa', 'Dirección Administrativa y Financiera') if pathname == '/administrativa' else
            create_direction_content('salud', 'Dirección de Salud Pública') if pathname == '/salud-publica' else
            create_direction_content('seguridad', 'Dirección de Seguridad Social') if pathname == '/seguridad-social' else
            create_direction_content('aseguramiento', 'Dirección de Aseguramiento') if pathname == '/aseguramiento' else
            create_home_content()
        ], className="mt-4 mb-4")
    ])
    
    return content

if __name__ == '__main__':
    app.run_server(debug=True)