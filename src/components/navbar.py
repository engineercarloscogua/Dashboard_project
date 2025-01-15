# Este módulo define la barra de navegación (Navbar) de la aplicación Dash.
# Proporciona enlaces de navegación hacia distintas secciones del dashboard.
# Se comunica con los callbacks de la aplicación para gestionar la navegación y el cierre de sesión.
# Este componente facilita el acceso a las diferentes áreas de la aplicación, mejorando la experiencia del usuario.

import dash_bootstrap_components as dbc  # Importa componentes de Bootstrap para Dash

# Función para crear la barra de navegación
def create_navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.Nav([
                # Enlace de navegación a la página de inicio
                dbc.NavItem(dbc.NavLink("Inicio", href="/", className="px-3")),
                
                # Menú desplegable con enlaces a diferentes direcciones
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Oficina Asesora Jurídica", href="/juridica"),  # Enlace a Jurídica
                        dbc.DropdownMenuItem("Oficina de Control Interno", href="/control-interno"),  # Enlace a Control Interno
                        dbc.DropdownMenuItem("Dirección Administrativa y Financiera", href="/administrativa"),  # Enlace a Administrativa
                        dbc.DropdownMenuItem("Dirección de Salud Pública", href="/salud-publica"),  # Enlace a Salud Pública
                        dbc.DropdownMenuItem("Dirección de Seguridad Social", href="/seguridad-social"),  # Enlace a Seguridad Social
                        dbc.DropdownMenuItem("Dirección de Aseguramiento", href="/aseguramiento"),  # Enlace a Aseguramiento
                    ],
                    nav=True,  # Permite integrar el menú en la barra de navegación
                    label="Direcciones",  # Título del menú desplegable
                    className="px-3",  # Estilo con espaciado horizontal
                ),
                
                # Botón para cerrar sesión
                dbc.NavItem(dbc.Button("Cerrar Sesión", id="logout-button", color="danger", size="sm", className="ms-2"))
            ], navbar=True)
        ],
        brand="Dashboard EPS",  # Nombre de la aplicación
        brand_href="/",  # Enlace del nombre hacia la página de inicio
        color="primary",  # Color principal de la barra
        dark=True,  # Tema oscuro para la barra
        className="mb-4",  # Margen inferior
    )
