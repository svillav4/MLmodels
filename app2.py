import streamlit as st
import pandas as pd
import seaborn as sns
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
st.side
