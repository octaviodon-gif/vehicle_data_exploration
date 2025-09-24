import pandas as pd
import plotly.express as px
import streamlit as st

# reading data into a dataframe
df_vehicles_us = pd.read_csv(
    'vehicles_us.csv')

# Streamlit application

st.title('Used Vehicles in the US')
st.write('This application is a Streamlit dashboard to analyze used vehicles in the US.')
st.dataframe(df_vehicles_us)

# create verification box for histogram or scatter plot

st.write('Please select the type of plot you want to build:')
build_scatterplot = st.checkbox('Construir un gráfico de dispersión')
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # if verification box is checked
    st.write('Construir un histograma para la columna odómetro')
    # asking user for check box to be histogram or scatter plot
    # create a histogram
    fig = px.histogram(df_vehicles_us, x="odometer")

    # showing an interactive Plotly chart
    st.plotly_chart(fig, use_container_width=True)


if build_scatterplot:  # if verification box is checked
    st.write('Construir un gráfico de dispersión para las columnas odómetro y precio')
    # create a scatter plot
    fig = px.scatter(df_vehicles_us, x="odometer", y="price")
    # showing an interactive Plotly chart
    st.plotly_chart(fig, use_container_width=True)


st.write('This application has been developed by Octavio Don as part of the TripleTen Data Science Bootcamp.')
st.write('GitHub repository: https://github.com/octaviodon-gif/tripleten_sprint_7_proyecto.git')
st.write('LinkedIn profile: https://www.linkedin.com/in/octavio-don-flores')
st.write('Portfolio: https://github.com/octaviodon')
