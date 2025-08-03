import openai
import fitz  # PyMuPDF
from dotenv import load_dotenv
import os
import pandas as pd
from io import StringIO
from prompt import prompt

# Cargar variables de entorno desde el archivo .env
load_dotenv(".env")

# Obtener la clave de API de OpenAI desde las variables de entorno
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def extraer_texto_pdf(ruta_pdf):

    doc = fitz.open(ruta_pdf)  # Abrir PDF
    text = "\n".join([page.get_text("text") for page in doc])  # Extraer texto
    return text


def estructurar_texto(texto):
    """Envía el texto a OpenAI y obtiene la respuesta estructurada en CSV,
    asegurando que solo devuelva datos válidos o 'error' en caso de problema."""

    cliente = openai.OpenAI(api_key=OPENAI_API_KEY)

    respuesta = cliente.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Eres un experto en extracción de datos de facturas. Devuelve solo el CSV sin explicaciones ni mensajes adicionales. Si no puedes extraer datos, devuelve exactamente la palabra 'error' sin comillas.",
            },
            {
                "role": "user",
                "content": prompt + "\n Este es el texto a parsear:\n" + texto,
            },
        ],
    )

    csv_respuesta = respuesta.choices[0].message.content.strip()
    return csv_respuesta


def csv_a_dataframe(csv):
    """Convierte el texto CSV en un DataFrame de pandas, asegurando que 'importe' sea numérico."""

    # Definir los tipos de datos para cada columna
    dtype_cols = {
        "fecha_factura": str,
        "proveedor": str,
        "concepto": str,
        "importe": str,  # Se leerá primero como str para poder limpiar comas
        "moneda": str,
    }

    # Leer el CSV en un DataFrame con los tipos especificados
    df_temp = pd.read_csv(StringIO(csv), delimiter=";", dtype=dtype_cols)

    # Convertir 'importe' a float, asegurando que los valores con coma se conviertan correctamente
    df_temp["importe"] = pd.to_numeric(
        df_temp["importe"].str.replace(",", "."), errors="coerce"
    )

    return df_temp
