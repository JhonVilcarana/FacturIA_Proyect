# 🤖 FacturIA -  Automatización Inteligente de Facturas

<div align="center">

![Python](https://img.shields.io/badge/python-v3.13+-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**Automatiza la lectura y análisis de facturas con IA, Python y Power BI**

*Transformando documentos no estructurados en datos estructurados con inteligencia artificial*

</div>

---

## 📋 Descripción

**FacturIA** es un sistema inteligente que automatiza completamente el procesamiento de facturas y documentos utilizando inteligencia artificial. El sistema extrae, estructura y almacena automáticamente la información de **cualquier tipo de archivo** (PDFs e imágenes), proporcionando una API REST para consultas y análisis posterior.

### ✨ Características Principales

- 🤖 **IA Avanzada**: Utiliza GPT-4o-mini para extraer información de facturas
- 📄 **Multi-formato**: Procesa PDFs y imágenes (JPEG, PNG, TIFF, BMP)
- �️ **OCR Inteligente**: Reconocimiento óptico de caracteres con Tesseract
- 💰 **Conversión de Monedas**: Convierte automáticamente USD a PEN (Soles)
- 🗄️ **Base de Datos**: Almacena datos en PostgreSQL para análisis posterior
- 🌐 **API REST**: Endpoint para consultar facturas procesadas
- 📈 **Dashboard Power BI**: Visualización avanzada de datos financieros
- 🌍 **Multiidioma**: Soporte para español e inglés en OCR
- 🔒 **Seguridad**: Gestión segura de credenciales con variables de entorno

---

## 🏗️ Arquitectura del Sistema

![Arquitectura del Sistema](FacturIA/Flujograma_FacturIA.png)

---
## 📊 Dashboard Power BI

Puedes explorar el dashboard interactivo publicado en Power BI:

![Dashboard FacturIA](FacturIA/Dashboard_FacturIA.png)

🔗 [Haz clic aquí para ver el dashboard en Power BI](https://app.powerbi.com/view?r=eyJrIjoiNGE3NDBlZDktMjY0NS00OWQ0LTk0ZDUtMWNjYzRlNGYxMTZhIiwidCI6ImNmYmQ4OGI0LTk0YmMtNGZiYS05OGJkLTY0ZDA3MjYzOTRhMyIsImMiOjR9)

El dashboard incluye indicadores clave como:

- 💰 Gastos por mes y año
- 🏢 Análisis por proveedor
- 📂 Categorización por concepto
- 📈 Tendencias temporales


---
## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.13+
- PostgreSQL
- Cuenta de OpenAI con API Key
- Tesseract OCR (para procesamiento de imágenes)
- Git

### 1. Clonar el Repositorio

```bash
git clone https://github.com/JhonVilcarana/Facturia_Proyect.git
cd Facturia_Proyect
```

### 2. Configurar Entorno Virtual

```bash
python -m venv .venv
source .venv/bin/activate  # En macOS/Linux
# .venv\Scripts\activate   # En Windows
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Instalar Tesseract OCR

**En macOS:**
```bash
brew install tesseract tesseract-lang
```

**En Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr tesseract-ocr-spa tesseract-ocr-eng
```

**En Windows:**
Descarga e instala desde: https://github.com/UB-Mannheim/tesseract/wiki

### 5. Configurar Variables de Entorno

```bash
cp .env.example .env
```

Edita el archivo `.env` con tus credenciales:

```env
OPENAI_API_KEY=tu_clave_openai_aqui
DATABASE_URL=postgresql+psycopg2://usuario:contraseña@host:puerto/database
```

### 6. Configurar Base de Datos

Asegúrate de que PostgreSQL esté ejecutándose y crea la base de datos necesaria.

---

## 💻 Uso

### Procesar Facturas

1. Coloca tus archivos en la carpeta `facturas/YYYY-MM/`:
   - **PDFs**: Facturas digitales nativas
   - **Imágenes**: JPG, JPEG, PNG, TIFF, BMP (facturas escaneadas)
2. Ejecuta el procesamiento:

```bash
python main.py
```

El sistema procesará automáticamente todos los formatos soportados usando:
- **PyMuPDF** para archivos PDF
- **Tesseract OCR** para imágenes (con reconocimiento en español e inglés)

### Iniciar API REST

```bash
python api_facturas.py
```

La API estará disponible en: `http://localhost:5050`

### Endpoints Disponibles

- **GET** `/facturas` - Obtiene todas las facturas procesadas

Ejemplo de respuesta:
```json
[
  {
    "id": 1,
    "concepto": "software",
    "fecha_factura": "2024-01-15",
    "importe": 299.99,
    "proveedor": "OpenAI LLC"
  }
]
```

---


## 📁 Estructura del Proyecto

```
FacturIA/
├── 📄 main.py                    # Script principal de procesamiento
├── 🔧 funciones.py               # Funciones auxiliares (PDF + OCR)
├── 🌐 api_facturas.py           # API REST
├── ⚙️ prompt.py                 # Prompts para OpenAI
├── 📋 requirements.txt          # Dependencias
├── 🔒 .env.example             # Plantilla de configuración
├── 📊 Dashboard_PowerBI/        # Dashboard y recursos
├── 📂 facturas/                # Facturas (PDFs e imágenes)
└── 📖 README.md                # Este archivo
```

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.13** - Lenguaje principal
- **Flask** - Framework web para API
- **SQLAlchemy** - ORM para base de datos
- **pandas** - Análisis de datos

### Procesamiento de Documentos
- **PyMuPDF (fitz)** - Extracción de texto de PDFs
- **Tesseract OCR** - Reconocimiento óptico de caracteres
- **Pillow (PIL)** - Procesamiento de imágenes
- **pytesseract** - Wrapper Python para Tesseract

### Inteligencia Artificial
- **OpenAI GPT-4o-mini** - Procesamiento de lenguaje natural
- **Structured Output** - Extracción de datos estructurados

### Base de Datos
- **PostgreSQL** - Base de datos principal
- **psycopg2** - Conector PostgreSQL

### Visualización
- **Power BI** - Dashboard y reportes
- **JSON API** - Intercambio de datos

---

## � Formatos Soportados

### 📄 Documentos PDF
- **Extracción**: Texto nativo usando PyMuPDF
- **Ventajas**: Alta precisión, procesamiento rápido
- **Ideal para**: Facturas digitales, documentos oficiales

### 🖼️ Imágenes
| Formato | Extensión | Descripción |
|---------|-----------|-------------|
| JPEG | `.jpg`, `.jpeg` | Facturas fotografiadas, escaneos comprimidos |
| PNG | `.png` | Screenshots, imágenes sin pérdida |
| TIFF | `.tiff` | Escaneos de alta calidad |
| BMP | `.bmp` | Imágenes bitmap sin compresión |

### 🌍 Idiomas OCR
- **Español** (`spa`): Reconocimiento optimizado para facturas latinoamericanas
- **Inglés** (`eng`): Soporte internacional
- **Combinado**: Detección automática español + inglés

---


### Procesamiento de IA
- Extracción inteligente de información de facturas multi-formato
- Identificación automática de campos (proveedor, fecha, importe, concepto)
- OCR avanzado con soporte multiidioma (español e inglés)
- Manejo de formatos de fecha diversos
- Detección automática de monedas

### Procesamiento de Documentos
- **PDFs**: Extracción directa de texto con PyMuPDF
- **Imágenes**: OCR con Tesseract para JPG, PNG, TIFF, BMP
- **Filtrado inteligente**: Ignora archivos ocultos y de sistema
- **Manejo de errores**: Procesamiento robusto con validaciones

### Gestión de Datos
- Conversión automática USD → PEN (factor 3.60)
- Validación de datos estructurados
- Almacenamiento incremental en PostgreSQL
- API REST para consultas en tiempo real

### Seguridad
- Variables de entorno para credenciales
- Exclusión de archivos sensibles en Git
- Validación de entrada de datos

---

## 📈 Casos de Uso

- **Empresas**: Automatización de contabilidad con documentos escaneados
- **Freelancers**: Gestión de gastos profesionales desde fotos móviles
- **Contadores**: Digitalización de documentos físicos y digitales
- **Analistas**: Extracción de insights financieros multi-formato
- **Desarrolladores**: Base para sistemas de facturación universales
- **Pymes**: Procesamiento de facturas sin restricciones de formato

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

---

## 👨‍💻 Autor

**Jhon Vilcarana**
- GitHub: [@JhonVilcarana](https://github.com/JhonVilcarana)
- Proyecto: [FacturIA](https://github.com/JhonVilcarana/Facturia_Proyect)

---

## 🙏 Agradecimientos

- OpenAI por la API de GPT-4o-mini
- Comunidad de Python por las excelentes librerías
- PostgreSQL por la robustez de la base de datos

---

<div align="center">

**⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub ⭐**

*Desarrollado con ❤️ y ☕ por Jhon Vilcarana*

</div>
