# Bridge Streamlit Application

Aplicación web para la gestión de servicios financieros de Unity Financial Services.

## Características

- Modificación de developer fees
- Creación de cuentas virtuales
- Gestión de direcciones de liquidación
- Interfaz intuitiva con Streamlit

## Despliegue en Railway

### Pasos para desplegar:

1. **Conectar repositorio a Railway:**
   - Ve a [Railway.app](https://railway.app)
   - Crea una nueva cuenta o inicia sesión
   - Haz clic en "New Project"
   - Selecciona "Deploy from GitHub repo"
   - Conecta tu repositorio de GitHub

2. **Configurar variables de entorno (opcional):**
   - En Railway, ve a la pestaña "Variables"
   - Agrega cualquier variable de entorno que necesites

3. **Desplegar:**
   - Railway detectará automáticamente que es una aplicación Python
   - Usará el `Procfile` para saber cómo ejecutar la aplicación
   - La aplicación estará disponible en la URL proporcionada por Railway

### Archivos de configuración incluidos:

- `requirements.txt`: Dependencias de Python
- `Procfile`: Instrucciones de ejecución para Railway
- `runtime.txt`: Versión de Python
- `.streamlit/config.toml`: Configuración de Streamlit

## Desarrollo local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
streamlit run FeeModification_app.py
```

## Estructura del proyecto

```
BridgeStreamlit/
├── FeeModification_app.py      # Aplicación principal
├── components/                 # Componentes reutilizables
├── screens/                    # Pantallas de la aplicación
├── utils/                      # Funciones utilitarias
└── Logo.png                    # Logo de la aplicación
``` 