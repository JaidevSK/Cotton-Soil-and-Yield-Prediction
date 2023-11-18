import joblib
import streamlit as st
import pandas as pd
import numpy as np

def predict(data):
  clf = joblib.load(“soilPredModel.sav”)
  return clf.predict(data)

st.write("Give the User Inputs")

ph = st.number_input('ph')
temp = st.number_input('Temperature')
humi = st.number_input('Humidity')
desn = st.number_input('Density')
elec = st.number_input('Electrical Conductivity')
nit = st.number_input('N')
phos = st.number_input('P')
pot = st.number_input('K')
cal = st.number_input('Ca')
mag = st.number_input('Mg')
grainsmmoth = st.number_input('Grain Surface Smoothness')
particlespacing = st.number_input('Particle Spacing')
partwidth = st.number_input('Particle Width')

a=predict(np.array([6.502985292, 20.87974371, 82.00274423, 0.92, 7.4, 100, 50,	43,	30,	19,	0, 1,	1]).reshape(1, -1))

if a[0] == 0:
  st.write("No Cotton")
elif a[0] == 1:
  st.write("Yes Cotton)
