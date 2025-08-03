# 🤖 FacturIA - Sistema Inteligente de Procesamiento de Facturas

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

**FacturIA** es un sistema inteligente que automatiza completamente el procesamiento de facturas PDF utilizando inteligencia artificial. El sistema extrae, estructura y almacena automáticamente la información de facturas, proporcionando una API REST para consultas y análisis posterior.

### ✨ Características Principales

- 🤖 **IA Avanzada**: Utiliza GPT-4o-mini para extraer información de facturas PDF
- 📊 **Procesamiento Automático**: Convierte texto no estructurado en datos estructurados
- 💰 **Conversión de Monedas**: Convierte automáticamente USD a SOL
- 🗄️ **Base de Datos**: Almacena datos en PostgreSQL para análisis posterior
- 🌐 **API REST**: Endpoint para consultar facturas procesadas
- 📈 **Dashboard Power BI**: Visualización avanzada de datos financieros
- 🔒 **Seguridad**: Gestión segura de credenciales con variables de entorno

---

## 🏗️ Arquitectura del Sistema

```
┌─────────────────┐    ┌──────────────┐    ┌────────────────┐
│   Facturas PDF  │───▶│   FacturIA   │───▶│   PostgreSQL   │
└─────────────────┘    │              │    └────────────────┘
                       │  + OpenAI    │           │
┌─────────────────┐    │  + Python    │    ┌────────────────┐
│   Power BI      │◀───│  + Flask     │───▶│   API REST     │
└─────────────────┘    └──────────────┘    └────────────────┘
```

---

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.13+
- PostgreSQL
- Cuenta de OpenAI con API Key
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

### 4. Configurar Variables de Entorno

```bash
cp .env.example .env
```

Edita el archivo `.env` con tus credenciales:

```env
OPENAI_API_KEY=tu_clave_openai_aqui
DATABASE_URL=postgresql+psycopg2://usuario:contraseña@host:puerto/database
```

### 5. Configurar Base de Datos

Asegúrate de que PostgreSQL esté ejecutándose y crea la base de datos necesaria.

---

## 💻 Uso

### Procesar Facturas

1. Coloca tus archivos PDF en la carpeta `facturas/YYYY-MM/`
2. Ejecuta el procesamiento:

```bash
python main.py
```

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

## 📊 Dashboard Power BI

El proyecto incluye un dashboard de Power BI (`Dashboard_PowerBI/Power_BI/FacturIA.pbix`) con visualizaciones de:

- 💰 Gastos por mes y año
- 🏢 Análisis por proveedor
- 📂 Categorización por concepto
- 📈 Tendencias temporales
- 💱 Análisis de conversión de monedas

---

## 📁 Estructura del Proyecto

```
FacturIA/
├── 📄 main.py                    # Script principal de procesamiento
├── 🔧 funciones.py               # Funciones auxiliares
├── 🌐 api_facturas.py           # API REST
├── ⚙️ prompt.py                 # Prompts para OpenAI
├── 📋 requirements.txt          # Dependencias
├── 🔒 .env.example             # Plantilla de configuración
├── 📊 Dashboard_PowerBI/        # Dashboard y recursos
├── 📂 facturas/                # Carpeta de facturas PDF
└── 📖 README.md                # Este archivo
```

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.13** - Lenguaje principal
- **Flask** - Framework web para API
- **SQLAlchemy** - ORM para base de datos
- **pandas** - Análisis de datos
- **PyPDF2** - Procesamiento de PDF

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

## 🔧 Funcionalidades Técnicas

### Procesamiento de IA
- Extracción inteligente de información de facturas
- Identificación automática de campos (proveedor, fecha, importe, concepto)
- Manejo de formatos de fecha diversos
- Detección automática de monedas

### Gestión de Datos
- Conversión automática USD → EUR (factor 0.9243)
- Validación de datos estructurados
- Almacenamiento incremental en PostgreSQL
- API REST para consultas en tiempo real

### Seguridad
- Variables de entorno para credenciales
- Exclusión de archivos sensibles en Git
- Validación de entrada de datos

---

## 📈 Casos de Uso

- **Empresas**: Automatización de contabilidad
- **Freelancers**: Gestión de gastos profesionales
- **Contadores**: Digitalización de documentos
- **Analistas**: Extracción de insights financieros
- **Desarrolladores**: Base para sistemas de facturación

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

**Jhon Vilcarana Tintaya**
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

*Desarrollado con ❤️ y ☕ por Jhon Vilcarana Tintaya*

</div>
