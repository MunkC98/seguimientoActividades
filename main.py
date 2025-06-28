import pandas as pd
import streamlit as st
import datetime as dt
import os

hoy = dt.date.today()
nombre_dia = hoy.strftime('%A')
path_data = 'data/data.csv'

st.title("Seguimiento de las actividades - " + f'{hoy}')

st.header(nombre_dia)

df = pd.read_csv(path_data)

st.write(df)