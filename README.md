# 🧾 FacturIA - Automatización Inteligente de Facturas con Python, GPT-4o, PostgreSQL y Power BI

**FacturIA** es un sistema automatizado que procesa, estructura y analiza facturas en PDF con distintos formatos utilizando Inteligencia Artificial. El objetivo es eliminar tareas manuales y acelerar el análisis financiero en empresas de cualquier tamaño.

---

## 🎯 Problema de Negocio

Las empresas reciben facturas con múltiples formatos, lo que dificulta su análisis. Tradicionalmente, extraer manualmente datos como proveedor, importe o fecha es costoso, propenso a errores y poco escalable. **FacturIA** resuelve esto integrando IA, automatización y visualización de datos en un flujo completo.

---

## 🚀 Flujo del Proyecto

```
📂 PDFs de Facturas
      ↓
🐍 Python: Extracción del texto
      ↓
🤖 GPT-4o (OpenAI): Estructuración de datos clave (fecha, proveedor, importe, etc.)
      ↓
📄 CSV → 📊 pandas DataFrame
      ↓
🧮 Conversión de moneda (USD → EUR)
      ↓
🗄 PostgreSQL: Almacenamiento en base de datos
      ↓
🌐 API REST (Flask)
      ↓
📈 Power BI: Visualización interactiva
```

---

## 🛠️ Tecnologías y Herramientas Utilizadas

### 🤖 Inteligencia Artificial
- **OpenAI GPT-4o-mini** – Extracción estructurada de texto desde facturas en PDF.
- **API de OpenAI** – Integración para análisis automatizado.

### 🐍 Programación y Librerías
- **Python 3.13**
- **pandas**, **sqlalchemy**, **flask**, **PyPDF2**, **dotenv**, **psycopg2**

### 🗄 Base de Datos
- **PostgreSQL** – Servidor remoto conectado desde Python (192.168.18.15)

### 🌐 Desarrollo Web
- **Flask API** – Endpoint `/facturas` para exponer los datos a Power BI.
- **JSON** – Intercambio de información entre servicios.

### 📊 Visualización
- **Power BI** – Dashboard con análisis mensual, top proveedores y distribución por concepto.

### ⚙️ Dev Tools
- **Git** / **GitHub** – Control de versiones y repositorio
- **VS Code**, **Terminal**, **pip**, **venv**

### 🔒 Seguridad
- **Variables de entorno (.env)** – Gestión segura de claves
- **.gitignore** – Exclusión de archivos sensibles

---

## 📁 Estructura del Repositorio

```
FacturIA/
├── app.py                 # API Flask (endpoint /facturas)
├── insertar_facturas.py  # Procesamiento principal de PDFs
├── funciones.py           # Funciones auxiliares
├── prompt.py              # Prompt personalizado para GPT-4o
├── .env                   # Configuración segura (no incluida en el repo)
├── requirements.txt       # Dependencias
├── /data                  # Carpeta para facturas o CSVs
└── /powerbi               # Archivos para construir el dashboard
```

---

## ⚙️ Instalación y Ejecución

```bash
git clone https://github.com/JhonVilcarana/Facturia_Proyect.git
cd FacturIA
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

1. Coloca tus facturas PDF en la carpeta `data/`
2. Ejecuta:

```bash
python insertar_facturas.py  # Procesa y carga datos en PostgreSQL
python main.py                # Levanta la API en http://localhost:5050/facturas
```

3. En Power BI: conéctate al endpoint JSON para visualizar.

---

## 📊 Dashboard Power BI

El dashboard incluye:

- Evolución mensual de gastos
- Gasto total y promedio por factura
- Ranking de proveedores
- Distribución por concepto

*(Ver carpeta `/powerbi` para plantilla y recursos visuales)*

---

## 🧠 Posibles Mejoras

- Fine-tuning del modelo con facturas propias
- OCR para facturas escaneadas (modelo de visión)
- Interfaz visual para usuarios no técnicos
- Conexión con ERP para combinar ingresos y generar cuenta de resultados

---

## 👨‍💻 Autor

**Jhon Vilcarana Atintaya**  
[GitHub](https://github.com/JhonVilcarana) · [LinkedIn](https://www.linkedin.com/) · [Portafolio](https://sites.google.com/)

---

## 📝 Licencia

MIT License - Libre para uso y modificación educativa o profesional.
