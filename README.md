# 🐉 CONSULTA-MORTAL4° en The Huddle, web scraping + base de datos.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣴⡾⣿⠛⠻⠉⠉⠙⠛⠛⠷⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣴⠟⠛⠧⣤⣝⣦⣤⣤⣤⣤⡀⠀⠀⠀⠉⠻⣶⣄⠀⠀⠀⠀
⠀⠀⠀⣴⠟⣡⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣷⣦⠀⠀⠀⠀⠻⣧⡀⠀⠀
⠀⢀⣾⠋⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣦⣄⣀⠀⠀⠀⠘⢿⡄⠀
⠀⣾⠇⢸⣿⣿⣿⣿⣿⡻⣿⣿⣿⡿⠦⣤⡀⠙⠻⣯⣽⣿⣿⡆⠀⠘⣿⡀
⢰⡿⠀⢿⣿⣿⣿⣿⣿⡏⠈⠉⠀⠀⠀⠀⠉⠳⣤⣀⣹⣫⡛⠀⠀⠀⢹⡇
⢸⡇⠀⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢀⣀⡈⠉⠉⠁⢷⠀⠀⢀⢸⡇
⠸⣷⠲⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠘⣧⢀⠴⣻⡇
⠀⢿⡄⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⠓⢈⣿⠁
⠀⠈⢿⡄⠀⠀⡿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⢀⣾⠃⠀
⠀⠀⠈⢻⣮⠙⠁⠀⠋⠉⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡿⠁⠀⠀
⠀⠀⠀⠀⠙⠿⣶⣦⣤⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

> *"Mini pipeline de datos real,  
flujo completo hasta el final.
Simula procesos con precisión,  
de inicio a fin, toda la conexión.  

Cada etapa corre sin tropiezo,  
del origen al destino va el progreso.  
Un viaje de datos que nunca se frena,  
con ritmo constante, como cadena."*

> **Scraping → Enriquecimiento → Persistencia → Modelado → Performance**.
---

## Descripción

**Consulta Mortal** un proyecto de datos con gran estrategia.  
De [Books to Scrape](https://books.toscrape.com/index.html) extrae la información,  
con web scraping inicia la operación.  

Luego APIs externas lo enriquecen,  
y en base relacional los datos se establecen.  
Al final consultas SQL avanzadas,  
dan vida al análisis con respuestas afinadas.
---

### 🗂️ Diagrama UML / Entidad-Relación (ER)

El modelo de datos sigue una estructura **relacional normalizada** con una tabla intermedia para resolver la relación **muchos a muchos** entre libros y autores:

- **`categorias`** → catálogo único de géneros (1 categoría → N libros).
- **`libros`** → entidad central con título, precio, calificación, URL y FK a `categorias`.
- **`autores`** → datos enriquecidos del autor (país, `api_external_id`, `api_source`, `created_at`).
- **`autor_libro`** → tabla pivote que conecta libros y autores (relación N:M).

> 🔗 **Relaciones:** `libros.categoria_id → categorias.id_categoria` y `autor_libro.id_libro/id_autor → libros/autores`.

![Diagrama Entidad-Relación](https://raw.githubusercontent.com/Astonete/web_scraping_challenge_4/refs/heads/main/UMLdiagrama%20entidad-relaci%C3%B3n%20(ER).jpg.jpeg)

---
## 📌 Pipeline de Web Scraping — Books to Scrape

> **Un pipeline es una secuencia automatizada de etapas que transforma datos crudos en información estructurada y almacenada.**

Este archivo `pipeline.ipynb` **extrae automáticamente libros, precios, calificaciones, categorías y autores desde `books.toscrape.com`, enriquece los datos de los autores consultando la API de Wikipedia, los almacena en una base de datos SQLite relacional y exporta los resultados a CSV**, incorporando caché de autores, reanudación del scraping por categoría, consultas SQL analíticas y pruebas de rendimiento con índices.

---

### 🧩 Etapas del pipeline

| # | Etapa | Descripción |
|---|-------|-------------|
| 1 | **Importación y configuración** | Librerías, sesión HTTP con reintentos y `User-Agent`. |
| 2 | **Funciones auxiliares** | Obtención de HTML, pausas, conexión a SQLite y caché de autores. |
| 3 | **Creación de la BD** | Tablas `categorias`, `libros`, `autores`, `autor_libro` e índices. |
| 4 | **Scraping** | Extracción de categorías, libros (con paginación) y autores. |
| 5 | **Enriquecimiento** | Búsqueda del autor y su país en Wikipedia con validación de nombres. |
| 6 | **Persistencia** | Inserción y actualización en SQLite evitando duplicados. |
| 7 | **Checkpoint** | Progreso en JSON y respaldo en CSV por categoría. |
| 8 | **Ejecución** | Scraping completo o reanudable con `continuar=True/False`. |
| 9 | **Consultas SQL** | Análisis: mejores libros, autores, categorías y países. |
| 10 | **Índices** | Comparación de rendimiento antes/después de indexar. |

---

### ⚙️ Tecnologías utilizadas

`Python` · `requests` · `BeautifulSoup` · `SQLite` · `pandas` · `Wikipedia API` · `Jupyter Notebook`

---

### 📂 Archivos generados

- `libreria.db` → Base de datos SQLite.
- `datos/cache_autores.csv` → Caché de autores enriquecidos.
- `datos/scraping_progreso.json` → Estado del scraping.
- `datos/libros_extraidos.csv` → Respaldo final de libros.
---
### 🔎 Consultas analíticas

El notebook incluye **8 consultas SQL** que explotan la base de datos para obtener información de valor:

| # | Consulta | Propósito |
|---|----------|-----------|
| 1 | Libros con >3 ★ y <£10 | Detectar lecturas buenas y baratas. |
| 2 | Autor con peor promedio (≥5 libros) | Identificar al autor peor valorado con muestra suficiente. |
| 3 | Categoría con mayor precio promedio | Ver qué género se cotiza más alto. |
| 4 | Top 5 autores con más libros | Medir prolificidad. |
| 5 | País con más libros con >3 ★ | Ranking geográfico por calidad. |
| 6 | Autores sin país registrado | Auditar la cobertura del enriquecimiento. |
| 7 | Ranking de autores por país | Usa `RANK() OVER (PARTITION BY …)` para posicionar autores dentro de cada país. |
| 8 | Libros más caros que el promedio de su categoría | Subconsulta correlacionada para detectar outliers de precio. |

---

### ⚡ Indexación y performance

Se comparó el tiempo de ejecución de una consulta por rango de precio (`precio_libro BETWEEN 20 AND 30`) **antes y después** de crear el índice `idx_libros_precio`:

| Escenario | Tiempo | Plan de ejecución |
|-----------|--------|-------------------|
| ❌ Sin índice | ~**0.0191 s** | `SCAN libros` (recorre toda la tabla). |
| ✅ Con índice | ~**0.0011 s** | `SEARCH libros USING INDEX idx_libros_precio` (acceso directo). |

> **Mejora ≈ 17× más rápido.** El índice evita el escaneo completo y permite localizar solo las filas que cumplen el rango, demostrando en la práctica el impacto de una buena estrategia de indexación.
---
### 📦 Librerías y dependencias

| Librería | Uso en el pipeline |
|----------|--------------------|
| `requests` | Peticiones HTTP al sitio y a la API de Wikipedia. |
| `beautifulsoup4` | Parseo del HTML (categorías, libros y autores). |
| `pandas` | Manejo de la caché de autores y exportación a CSV. |
| `sqlite3` | Base de datos relacional (incluida en Python). |
| `urllib3` | Reintentos automáticos vía `Retry` + `HTTPAdapter`. |
| `json`, `re`, `os`, `time`, `hashlib`, `datetime`, `typing` | Utilidades estándar (incluidas en Python). |

> ⚠️ Solo `requests`, `beautifulsoup4` y `pandas` son externas; el resto viene con Python 3.11+.

---

### 🚀 Instalación

**1. Clona el repositorio**
```bash
git clone <https://github.com/Astonete/web_scraping_challenge_4>
cd <web_scraping_challenge_4>

---

---

### 👤 Autor

**Daniel Molinas** — Estudiante de Penguin Academy  
Challenge desarrollado como parte del programa de formación.

---