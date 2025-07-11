import streamlit as st
import pandas as pd

# Importar componentes y pantallas
from components.header import show_header
from screens.home_screen import show_home_screen
from screens.fee_modification_screen import show_fee_modification_screen
from screens.contact_screen import show_contact_screen
from screens.virtual_account_screen import show_virtual_account_screen

def main():
    """Función principal de la aplicación"""
    
    # Configuración de la página
    st.set_page_config(
        page_title="Unity Financial Services",
        page_icon="💰",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Mostrar header en todas las pantallas
    show_header()
    
    # Sidebar para selección de pantalla
    st.sidebar.markdown("## Navegación")
    pantalla = st.sidebar.selectbox(
        "Selecciona una pantalla", 
        ["Inicio", "Modificacion Fee", "Crear virtual account", "Contacto"]
    )
    
    # Información adicional en el sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Información")
    st.sidebar.markdown("**Versión**: 1.0.0")
    st.sidebar.markdown("**Desarrollado por**: Unity Financial Services")
    
    # Mostrar la pantalla correspondiente
    if pantalla == "Inicio":
        show_home_screen()
    elif pantalla == "Modificacion Fee":
        show_fee_modification_screen()
    elif pantalla == "Crear virtual account":
        show_virtual_account_screen()
    elif pantalla == "Contacto":
        show_contact_screen()

if __name__ == "__main__":
    main()
