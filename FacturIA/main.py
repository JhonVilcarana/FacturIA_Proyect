import funciones
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Crear un DataFrame vacío para almacenar todas las facturas
df = pd.DataFrame()

# Recorrer todas las carpetas dentro de la carpeta "facturas"
for carpeta in sorted(os.listdir("./facturas")):
    ruta_carpeta = os.path.join("./facturas/", carpeta)
    if not os.path.isdir(ruta_carpeta):
        continue  # Ignorar si no es una carpeta

    # Recorrer todos los archivos dentro de la carpeta
    for archivo in os.listdir(ruta_carpeta):
        # Saltar archivos ocultos y de sistema
        if archivo.startswith('.'):
            continue
            
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        
        # Solo procesar archivos (no carpetas)
        if os.path.isfile(ruta_archivo):
            print(f"📄 Procesando archivo: {ruta_archivo}")

            # Extraer texto del archivo (PDF o imagen)
            texto_no_estructurado = funciones.extraer_texto_archivo(ruta_archivo)
            
            # Si no se pudo extraer texto, continuar con el siguiente archivo
            if not texto_no_estructurado.strip():
                print(f"⚠️ No se pudo extraer texto de: {archivo}")
                continue

            # Estructurar el texto de la factura
            texto_estructurado = funciones.estructurar_texto(texto_no_estructurado)
            
            # Verificar si OpenAI devolvió un error
            if texto_estructurado.lower().strip() == 'error':
                print(f"❌ Error al estructurar el texto de: {archivo}")
                continue

            # Convertir texto estructurado en dataframe
            try:
                df_factura = funciones.csv_a_dataframe(texto_estructurado)
                
                # Verificar que el dataframe no esté vacío
                if not df_factura.empty:
                    # Anexar el dataframe de la factura al dataframe general
                    df = pd.concat([df, df_factura], ignore_index=True)
                    print(f"✅ Procesado exitosamente: {archivo}")
                else:
                    print(f"⚠️ DataFrame vacío para: {archivo}")
            except Exception as e:
                print(f"❌ Error al convertir a DataFrame: {archivo} - {str(e)}")
                continue

# Si la moneda es "dolares" convertir a soles multiplicando por el tipo de cambio USD a PEN
df.loc[df["moneda"] == "dolares", "importe"] *= 3.75  # Tipo de cambio aproximado USD a PEN

# Eliminar las columnas no esenciales
df = df.iloc[:, 0:4]

# Guardar el DataFrame final en una bbdd postgres
# Crear una conexión a la base de datos PostgreSQL
database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)

# Guardar el DataFrame en PostgreSQL
df.to_sql("facturas", engine, if_exists="append", index=False)

# Cerrar conexión
engine.dispose()

print("Proceso de extracción y estructuración de facturas completado exitosamente.")
print("Datos guardados en la base de datos 'facturas.db'.")
