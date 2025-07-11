import pandas as pd
import os
from datetime import datetime

def save_fee_log(customer_id, liq_address, fee_val, status_code, response_text, csv_file="registro_fees.csv"):
    """
    Guarda un registro de la operación de modificación de fee en un archivo CSV.
    
    Args:
        customer_id (str): ID del cliente
        liq_address (str): Dirección de liquidación
        fee_val (str): Valor del fee
        status_code (int): Código de estado de la respuesta
        response_text (str): Texto de respuesta de la API
        csv_file (str): Nombre del archivo CSV (por defecto: registro_fees.csv)
    """
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "customer_id": customer_id,
        "liq_address": liq_address,
        "fee_val": fee_val,
        "status_code": status_code,
        "response": response_text
    }

    df_log = pd.DataFrame([log_entry])
    
    try:
        if os.path.isfile(csv_file):
            df_log.to_csv(csv_file, mode='a', header=False, index=False)
        else:
            df_log.to_csv(csv_file, index=False)
        return True
    except Exception as e:
        print(f"Error al guardar el log: {e}")
        return False

def get_fee_logs(csv_file="registro_fees.csv", limit=50):
    """
    Obtiene los registros de fees desde el archivo CSV.
    
    Args:
        csv_file (str): Nombre del archivo CSV
        limit (int): Número máximo de registros a retornar
    
    Returns:
        pandas.DataFrame: DataFrame con los registros
    """
    try:
        if os.path.isfile(csv_file):
            df = pd.read_csv(csv_file)
            return df.tail(limit)
        else:
            return pd.DataFrame()
    except Exception as e:
        print(f"Error al leer el archivo de logs: {e}")
        return pd.DataFrame() 