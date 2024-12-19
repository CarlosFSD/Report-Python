import streamlit as st
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium

# Título del dashboard
st.title("Dashboard interactivo con Matplotlib y Folium")

# Sección de gráficos de Matplotlib
st.subheader("Gráfico interactivo")
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

fig, ax = plt.subplots()
ax.plot(x, y, marker='o', linestyle='-', color='b', label='Datos de ejemplo')
ax.set_title("Gráfico de ejemplo")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.legend()

st.pyplot(fig)  # Mostrar gráfico en Streamlit

# Sección de mapas interactivos con Folium
st.subheader("Mapa interactivo")
mapa = folium.Map(location=[19.4326, -99.1332], zoom_start=10)  # Ciudad de México
folium.Marker([19.4326, -99.1332], popup="CDMX").add_to(mapa)

# Mostrar mapa en Streamlit
st_folium(mapa, width=700, height=500)

# Agregar widgets interactivos
st.sidebar.header("Opciones de usuario")
opcion = st.sidebar.selectbox("Selecciona una opción:", ["Gráfico", "Mapa", "Ambos"])
st.write(f"Mostrando: {opcion}")
