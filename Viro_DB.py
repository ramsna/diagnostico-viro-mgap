import streamlit
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
# Definir los datos para el gráfico
enfermedades = ['Arteritis Viral Equina', 'Encefalitis']

# Configuración de la página de Streamlit
page_title = "Capacidad diagnóstica del laboratorio de Virologia MGAP"
page_icon = "🦠"
layout = 'centered'
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

# Título de la página
st.title(page_title + " " + page_icon)

BD = pd.read_csv("C:\\Users\\micmg\\Documents\\Proyecto Base de Datos\\Capacidad Diagnostica Viro.csv", encoding='ISO-8859-1')
print(BD.head())



# Interfaz de la aplicación
st.title("Base de Datos de Enfermedades")
enfermedad_seleccionada = st.selectbox("Selecciona una enfermedad:", list(BD.Enfermedad))


# Mostrar características de la enfermedad seleccionada
if enfermedad_seleccionada:
    # Interfaz de la aplicación
    st.subheader("Características de " + enfermedad_seleccionada)
    caracteristica_seleccionada = st.selectbox("Selecciona una caracteristica:", list(BD.columns[1:]))
    dato=BD[BD['Enfermedad']==enfermedad_seleccionada][caracteristica_seleccionada]
    st.write(f"{dato.values[0]}")
