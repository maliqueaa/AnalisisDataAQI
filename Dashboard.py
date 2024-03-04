import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set_theme(style="black")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Dataset
df_airquality = pd.read_csv("https://raw.githubusercontent.com/FOLZi-4G/Analisis-Data-Dicoding/main/dashboard/main_data.csv")

# Min dan Max data
min_date = pd.to_datetime(pd.to_datetime(df_airquality["date"].min()).strftime("%Y-%m-%d"))
max_date = pd.to_datetime(pd.to_datetime(df_airquality["date"].max()).strftime("%Y-%m-%d"))

with st.sidebar:
    # Title di web
    st.title("Analisis Kualitas Udara")
    # add logo
    st.image("https://raw.githubusercontent.com/FOLZi-4G/Analisis-Data-Dicoding/main/Python_Meter.jpg")

    
    # Get start_date & end_date from date_input
    start_date, end_date = st.date_input(
        label='Pilih rentang waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
