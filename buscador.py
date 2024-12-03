import pandas as pd
import streamlit as st

# URL del archivo Excel en GitHub
url = "https://raw.githubusercontent.com/manuoctopus/COMPLAINTS/main/cp00.xlsx"

# Cargar el archivo Excel desde GitHub
df = pd.read_excel(url)

# Título de la aplicación
st.title("Buscador de Complaint")

# Ingreso de consulta
consulta = st.text_input("Escribe tu palabra clave o frase:")

if consulta:
    # Filtrar los resultados que contienen la consulta en la columna 'Palabras Clave'
    resultados = df[df['Palabras Clave'].str.contains(consulta, case=False, na=False)]

    if not resultados.empty:
        # Mostrar los resultados con las columnas 'Categoría' y 'Subtipo'
        st.write("Resultados encontrados:")
        st.write(resultados[['Categoría', 'Subtipo']])
    else:
        st.write("No se encontró ninguna coincidencia.")
