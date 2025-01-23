import pickle
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import warnings
warnings.filterwarnings("ignore")

model = pickle.load(open('C:/Users/K SHANMUKH/OneDrive/Desktop/Co2_Forecasting/forecast_model.pickle', 'rb'))
df = pd.read_excel("CO2 dataset.xlsx")
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index(['Year'], inplace=True)

st.set_page_config(layout='centered')

image = Image.open('C:/Users/K SHANMUKH/OneDrive/Desktop/Co2_Forecasting/istockphoto-1390027486-612x612.jpg')  # Replace with your image path
st.image(image)

year = st.slider("Select number of Years", 1, 30, step=1)

# Prediction
pred = model.forecast(year)
pred = pd.DataFrame(pred, columns=['CO2'])

if st.button("Predict"):
    col1, col2 = st.columns([2, 3])
    with col1:
        st.dataframe(pred)  
    with col2:
        fig, ax = plt.subplots()
        df['CO2'].plot(style='--', color='gray', label='Historical Data')
        pred['CO2'].plot(color='blue', label='Predicted CO2')
        ax.set_title("CO2 Emissions Forecast")
        ax.set_xlabel('Year')
        ax.set_ylabel('CO2 Emissions')
        ax.legend()
        st.pyplot(fig)
