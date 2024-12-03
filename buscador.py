import pandas as pd
import streamlit as st

# URL del archivo Excel en GitHub
url = "https://raw.githubusercontent.com/manuoctopus/COMPLAINTS/main/cp00.xlsx"

# Cargar el archivo Excel desde GitHub
df = pd.read_excel(url)

# Mostrar los primeros 5 registros (opcional)
st.write("Datos cargados desde el archivo Excel:")
st.write(df.head())

# Tu lógica de consulta y búsqueda en el DataFrame
consulta = st.text_input("Escribe tu octo-consulta:")

if consulta:
    # Filtrar los resultados que coinciden con la consulta
    resultados = df[df['Palabras Clave'].str.contains(consulta, case=False, na=False)]

    if not resultados.empty:
        st.write("Categoría y Subtipo correspondiente:")
        st.write(resultados[['Categoría', 'Subtipo']])
    else:
        st.write("No se encontró coincidencia.")
