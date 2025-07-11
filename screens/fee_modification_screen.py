import streamlit as st
import pandas as pd
from utils.api_functions import get_liquidation_address_id, update_developer_fee
from utils.logging_functions import save_fee_log

def show_fee_modification_screen():
    """Pantalla de modificación de developer fee"""
    st.markdown("### Developer fee")
    
    # Información adicional
    st.info("Esta herramienta te permite actualizar el developer fee para direcciones de liquidación específicas.")

    # Crear layout de dos columnas
    col1, col2 = st.columns([1, 1])
    
    # Variable para almacenar la información de la dirección
    liq_address_info = None
    
    with col1:
        st.markdown("#### Formulario de actualización")
        # --- Entradas del formulario ---
        with st.form("fee_modification_form"):
            customer_id = st.text_input("Customer ID", help="Ingresa el UUID del cliente")
            liq_address = st.text_input("Wallet/Liquidation address", help="Ingresa la dirección de wallet o liquidación")
            fee_val = st.text_input("Developer Fee", help="Ingresa el fee como porcentaje (ej: 2.5)")
            api_key = st.text_input("API Key", type="password", help="Ingresa tu clave de API")
            
            submitted = st.form_submit_button("Update developer fee")
        
        # --- Procesar formulario ---
        if submitted:
            if not all([customer_id, liq_address, fee_val, api_key]):
                st.error("❌ Hay campos vacíos. Por favor completa todos los campos.")
            else:
                with st.spinner("Procesando solicitud..."):
                    # Obtener ID de la dirección de liquidación
                    liq_address_info = get_liquidation_address_id(customer_id, liq_address, api_key)
                    
                    if liq_address_info is None or liq_address_info.get("count", 0) == 0:
                        st.error("❌ No se pudo encontrar la dirección de liquidación. Verifica los datos ingresados.")
                    else:
                        # Obtener el primer elemento de la lista de datos
                        liq_address_data = liq_address_info.get("data", [])[0] if liq_address_info.get("data") else None
                        liq_address_ID = liq_address_data.get("id") if liq_address_data else None
                        
                        if liq_address_ID is None:
                            st.error("❌ No se pudo obtener el ID de la dirección de liquidación.")
                        else:
                            # Actualizar developer fee
                            status_code, response_text, success = update_developer_fee(
                                customer_id, liq_address_ID, fee_val, api_key
                            )
                            
                            if success:
                                st.subheader("Respuesta de la API")
                                st.code(response_text)
                                
                                # Guardar registro en CSV
                                log_saved = save_fee_log(
                                    customer_id, liq_address, fee_val, status_code, response_text
                                )
                                
                                if status_code == 200:
                                    st.success("✅ Developer fee actualizado exitosamente.")
                                    if log_saved:
                                        st.info("📝 Registro guardado en el archivo de logs.")
                                else:
                                    st.warning(f"⚠️ La operación se completó pero con código de estado: {status_code}")
                            else:
                                st.error(f"❌ Error inesperado: {response_text}")
    
    with col2:
        st.markdown("#### Información de la dirección de liquidación")
        
        # Mostrar información de la dirección si está disponible
        if liq_address_info and liq_address_info.get("count", 0) > 0:
            liq_address_data = liq_address_info.get("data", [])[0]
            
            # Crear un DataFrame para mostrar los datos de forma organizada
            info_data = {
                "Campo": [
                    "ID", "Currency", "Chain", "Customer ID", "External Account ID",
                    "Prefunded Account ID", "Destination Payment Rail", "Destination Currency",
                    "Address", "Destination Address", "State", "Created At", "Updated At"
                ],
                "Valor": [
                    liq_address_data.get("id", "N/A"),
                    liq_address_data.get("currency", "N/A"),
                    liq_address_data.get("chain", "N/A"),
                    liq_address_data.get("customer_id", "N/A"),
                    liq_address_data.get("external_account_id", "N/A"),
                    liq_address_data.get("prefunded_account_id", "N/A"),
                    liq_address_data.get("destination_payment_rail", "N/A"),
                    liq_address_data.get("destination_currency", "N/A"),
                    liq_address_data.get("address", "N/A"),
                    liq_address_data.get("destination_address", "N/A"),
                    liq_address_data.get("state", "N/A"),
                    liq_address_data.get("created_at", "N/A"),
                    liq_address_data.get("updated_at", "N/A")
                ]
            }
            
            info_df = pd.DataFrame(info_data)
            st.dataframe(info_df, use_container_width=True, hide_index=True)
            
            # Mostrar campos adicionales si están presentes
            additional_fields = []
            if liq_address_data.get("destination_wire_message"):
                additional_fields.append(f"**Wire Message:** {liq_address_data['destination_wire_message']}")
            if liq_address_data.get("destination_sepa_reference"):
                additional_fields.append(f"**SEPA Reference:** {liq_address_data['destination_sepa_reference']}")
            if liq_address_data.get("destination_spei_reference"):
                additional_fields.append(f"**SPEI Reference:** {liq_address_data['destination_spei_reference']}")
            if liq_address_data.get("destination_ach_reference"):
                additional_fields.append(f"**ACH Reference:** {liq_address_data['destination_ach_reference']}")
            if liq_address_data.get("destination_blockchain_memo"):
                additional_fields.append(f"**Blockchain Memo:** {liq_address_data['destination_blockchain_memo']}")
            if liq_address_data.get("return_address"):
                additional_fields.append(f"**Return Address:** {liq_address_data['return_address']}")
            
            if additional_fields:
                st.markdown("#### Información adicional")
                for field in additional_fields:
                    st.markdown(field)
        else:
            st.info("👈 Completa el formulario y envía para ver la información de la dirección de liquidación.")
    
    # Mostrar historial de operaciones
    st.markdown("---")
    st.markdown("### Historial de operaciones recientes")
    
    try:
        from utils.logging_functions import get_fee_logs
        logs_df = get_fee_logs(limit=10)
        
        if not logs_df.empty:
            # Formatear la tabla para mejor visualización
            display_df = logs_df.copy()
            display_df['timestamp'] = pd.to_datetime(display_df['timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')
            display_df = display_df[['timestamp', 'customer_id', 'liq_address', 'fee_val', 'status_code']]
            display_df.columns = ['Fecha', 'Customer ID', 'Dirección', 'Fee', 'Estado']
            
            st.dataframe(display_df, use_container_width=True)
        else:
            st.info("No hay registros de operaciones previas.")
    except Exception as e:
        st.warning(f"No se pudieron cargar los registros: {e}") 