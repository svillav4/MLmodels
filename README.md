# Proyecto de Modelos Supervisados con Streamlit

Este proyecto implementa diferentes modelos de **aprendizaje supervisado** (clasificación y regresión) y los despliega en una aplicación interactiva construida con **Streamlit**.  
El objetivo es permitir al usuario cargar datos, entrenar modelos, ajustar hiperparámetros y visualizar métricas de rendimiento en una interfaz web sencilla.

---

## 🚀 Funcionalidades
- Carga de datasets en formato `.csv`.
- Selección de modelos supervisados (Regresión Lineal, Regresión Logística, Árboles de Decisión, Random Forest, SVM, KNN, etc.).
- División automática en conjuntos de entrenamiento y prueba.
- Ajuste de hiperparámetros desde la interfaz.
- Visualización de métricas (accuracy, precision, recall, RMSE, etc.).
- Gráficos interactivos para análisis de resultados.

---

## 🛠️ Tecnologías utilizadas
- **Python 3.9+**
- **Streamlit** – Despliegue de la aplicación web.
- **Scikit-learn** – Implementación de modelos supervisados.
- **Pandas** – Manipulación y análisis de datos.
- **NumPy** – Operaciones numéricas.
- **Matplotlib / Seaborn** – Visualización de datos y métricas.

---

## 📦 Requisitos de instalación
Antes de ejecutar el proyecto, asegúrate de tener instalado **Python 3.9+**.  
Luego, instala las dependencias necesarias:

```bash
pip install -r requirements.txt