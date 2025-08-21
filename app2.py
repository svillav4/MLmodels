import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Análisis Exploratorio de Datos - Agricultura", layout="wide")

st.title("Análisis Exploratorio de Datos (EDA) con Dataset de Agricultura")

# Cargar dataset
@st.cache_data
def cargar_datos():
    return pd.read_csv("dataset_agricultura.csv")

try:
    df = cargar_datos()
    st.success("Dataset cargado correctamente.")
except FileNotFoundError:
    st.error("No se encontró el archivo 'dataset_agricultura.csv'. Asegúrate de que esté en la misma carpeta que app2.py.")
    st.stop()

# Vista previa de los datos
st.subheader("Vista previa de los datos")
st.dataframe(df.head(10))

# Información general
st.subheader("Información general del dataset")
st.write(f"El dataset contiene {df.shape[0]} filas y {df.shape[1]} columnas.")

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
        df.plot(x=x_axis, y=y_axis, kind="line", ax=ax)
    else:
        st.warning("Necesitas seleccionar una variable Y para este gráfico.")

elif tipo_grafico == "Barras":
    if y_axis:
        df.plot(x=x_axis, y=y_axis, kind="bar", ax=ax)
    else:
        df[x_axis].value_counts().plot(kind="bar", ax=ax)

elif tipo_grafico == "Dispersión":
    if y_axis:
        df.plot(x=x_axis, y=y_axis, kind="scatter", ax=ax)
    else:
        st.warning("Necesitas seleccionar una variable Y para este gráfico.")

elif tipo_grafico == "Histograma":
    df[x_axis].plot(kind="hist", bins=20, ax=ax)

elif tipo_grafico == "Pastel":
    df[x_axis].value_counts().plot(kind="pie", autopct='%1.1f%%', ax=ax)

st.pyplot(fig)
