import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Buscador de Categorías")

# Campo de entrada de texto para la consulta
consulta = st.text_input("Escribe tu consulta:")

if consulta:
    # Cargar el archivo Excel
    excel_file = st.file_uploader("Sube tu archivo Excel", type=["xlsx", "xls"])

    if excel_file is not None:
        # Leer el archivo Excel
        df = pd.read_excel(excel_file)

        # Buscar la consulta en las palabras clave (ajusta las columnas según tu archivo)
        categoria_subtipo = df[df['Palabras Clave'].str.contains(consulta, case=False, na=False)]

        # Mostrar el resultado
        if not categoria_subtipo.empty:
            st.write("Categoría y Subtipo encontrados:")
            st.write(categoria_subtipo[['Categoría', 'Subtipo']])
        else:
            st.write("No se encontró coincidencia con la consulta.")
    else:
        st.write("Por favor, sube un archivo Excel.")
else:
    st.write("Por favor, ingresa una consulta.")

