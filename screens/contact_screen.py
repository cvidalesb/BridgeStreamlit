import streamlit as st

def show_contact_screen():
    """Pantalla de contacto"""
    st.markdown("## Contacto")
    st.markdown("Información de contacto de Unity Financial Services")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Soporte técnico")
        st.markdown("- **Soporte API**: api-support@unityfinancial.com")
        st.markdown("- **Documentación**: docs.unityfinancial.com")
        st.markdown("- **Estado del servicio**: status.unityfinancial.com")
    """
    with col1:
        st.markdown("### Información de contacto")
        st.markdown("- **Email**: contacto@unityfinancial.com")
        st.markdown("- **Teléfono**: +1-555-0123")
        st.markdown("- **Dirección**: 123 Financial Street, Suite 100")
        st.markdown("- **Horario**: Lunes a Viernes 9:00 AM - 6:00 PM")
    
    with col2:
        st.markdown("### Soporte técnico")
        st.markdown("- **Soporte API**: api-support@unityfinancial.com")
        st.markdown("- **Documentación**: docs.unityfinancial.com")
        st.markdown("- **Estado del servicio**: status.unityfinancial.com")
    """
    st.markdown("---")
    st.markdown("*¿Necesitas ayuda? Nuestro equipo está disponible para asistirte.*") 