import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos



st.header('Graficos en linea')

hist_button = st.button('Construir histograma') 
disp_button = st.button('Construir grafico de dispersion')

        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión (ajustar columnas según tus datos)
    fig_scatter = px.scatter(car_data, x='odometer', y='price')  # Reemplaza 'odometer' y 'price' con las columnas correctas
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)