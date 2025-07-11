import streamlit as st

def show_header():
    """Muestra el header con logo y título"""
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("UNITY FINANCIAL SERVICES")
    with col2:
        try:
            st.image("Logo.png", use_container_width=True)
        except:
            st.warning("No se encontró la imagen 'Logo.png'")
    
    st.markdown("---") 