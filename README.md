# Buscador Streamlit

Este proyecto es una aplicación web construida con **Streamlit** que permite realizar consultas para encontrar la **categoría** y **subtipo** más adecuados basados en una **palabra clave** o **ejemplo**. El archivo Excel que contiene las relaciones de palabras clave, categorías y subtipos solo necesita ser cargado una vez, y la aplicación utilizará esta información para realizar las consultas posteriores.

## Requisitos

Para ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias:

- **Python 3.x**
- **Streamlit**: Para crear la interfaz web.
- **Pandas**: Para manipular datos del archivo Excel.
- **Openpyxl**: Para leer archivos Excel en formato `.xlsx`.

Puedes instalar estas dependencias ejecutando:

```bash
pip install -r requirements.txt
