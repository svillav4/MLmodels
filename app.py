import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from faker import Faker
import random

# Inicializar Faker
fake = Faker()

# Función para generar datos sintéticos deportivos
def generar_datos_deportivos(n_filas, n_columnas):
    variables = {
        "Nombre_Jugador": [fake.first_name() for _ in range(n_filas)],
        "Deporte": [random.choice(["Fútbol", "Baloncesto", "Tenis", "Natación", "Ciclismo"]) for _ in range(n_filas)],
        "Edad": np.random.randint(15, 40, n_filas),
        "País": [fake.country() for _ in range(n_filas)],
        "Altura_cm": np.round(np.random.normal(175, 10, n_filas), 1),
        "Peso_kg": np.round(np.random.normal(70, 12, n_filas), 1),
        "Partidos_Jugados": np.random.randint(1, 200, n_filas),
        "Puntos_Anotados": np.random.randint(0, 5000, n_filas),
        "Porcentaje_Victorias": np.round(np.random.uniform(0.2, 1.0, n_filas), 2),
        "Equipo": [random.choice(["Equipo A", "Equipo B", "Equipo C", "Equipo D"]) for _ in range(n_filas)]
    }

    columnas_seleccionadas = list(variables.keys())[:n_columnas]
    datos = {col: variables[col] for col in columnas_seleccionadas}
    return pd.DataFrame(datos)

# Configuración de la página
st.set_page_config(page_title="Análisis Exploratorio de Datos - Deportes", layout="wide")

st.title("Análisis Exploratorio de Datos (EDA) con Datos Deportivos Sintéticos")

# Barra lateral: configuración de los datos
st.sidebar.header("Configuración de datos")
n_filas = st.sidebar.slider("Número de muestras", min_value=50, max_value=500, value=200, step=50)
n_columnas = st.sidebar.slider("Número de columnas", min_value=3, max_value=10, value=6)

# Generar datos
df = generar_datos_deportivos(n_filas, n_columnas)

# Mostrar tabla
st.subheader("Vista previa de los datos")
st.dataframe(df.head(10))

# Mostrar estadísticas
if st.checkbox("Mostrar estadísticas descriptivas"):
    st.write(df.describe(include="all"))

# Selección de variables
st.sidebar.header("Selección de variables")
columnas = df.columns.tolist()
x_axis = st.sidebar.selectbox("Variable en eje X", options=columnas)
y_axis = st.sidebar.selectbox("Variable en eje Y (opcional)", options=[None] + columnas)

# Selección del tipo de gráfico
st.sidebar.header("Tipo de gráfico")
tipo_grafico = st.sidebar.selectbox("Selecciona un gráfico", ["Línea", "Barras", "Dispersión", "Histograma", "Pastel"])

st.subheader(f"Visualización: {tipo_grafico}")

# Graficar según la selección
fig, ax = plt.subplots(figsize=(8, 5))

if tipo_grafico == "Línea":
    if y_axis:
        sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
    else:
        st.warning("Necesitas seleccionar una variable Y para este gráfico.")

elif tipo_grafico == "Barras":
    if y_axis:
        sns.barplot(data=df, x=x_axis, y=y_axis, ax=ax)
    else:
        df[x_axis].value_counts().plot(kind="bar", ax=ax)

elif tipo_grafico == "Dispersión":
    if y_axis:
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
    else:
        st.warning("Necesitas seleccionar una variable Y para este gráfico.")

elif tipo_grafico == "Histograma":
    sns.histplot(df[x_axis], bins=20, kde=True, ax=ax)

elif tipo_grafico == "Pastel":
    df[x_axis].value_counts().plot(kind="pie", autopct='%1.1f%%', ax=ax)

st.pyplot(fig)
