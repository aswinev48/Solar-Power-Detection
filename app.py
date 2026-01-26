#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model and scalers
model = pickle.load(open("gbr_model.pkl", "rb"))
scaler_features = pickle.load(open("scaler_features.pkl", "rb"))
scaler_target = pickle.load(open("scaler_target.pkl", "rb"))

st.title("☀️ Solar Power Predictor (Dynamic Ranges)")

# Use columns for a better layout
col1, col2 = st.columns(2)

with col1:
    # distance-to-solar-noon: min 0.05, max 1.14
    dist_noon = st.slider("Distance to Solar Noon", 
                          min_value=0.05, max_value=1.15, value=0.50, step=0.01)
    
    # temperature: min 42, max 78
    temp = st.slider("Temperature (°F)", 
                     min_value=40.0, max_value=80.0, value=58.0, step=1.0)
    
    # wind-direction: min 1, max 36
    wind_dir = st.slider("Wind Direction", 
                         min_value=1.0, max_value=36.0, value=25.0, step=1.0)
    
    # wind-speed: min 1.1, max 26.6
    wind_speed = st.slider("Wind Speed (mph)", 
                           min_value=1.0, max_value=27.0, value=10.0, step=0.1)

with col2:
    # sky-cover: min 0, max 4
    sky_cover = st.slider("Sky Cover", 
                          min_value=0, max_value=4, value=2, step=1)
    
    # humidity: min 14, max 100
    humidity = st.slider("Humidity (%)", 
                         min_value=10, max_value=100, value=73, step=1)
    
    # average-wind-speed-(period): min 0, max 40
    avg_wind = st.slider("Avg Wind Speed (Period)", 
                         min_value=0.0, max_value=40.0, value=10.0, step=0.1)
    
    # average-pressure-(period): min 29.48, max 30.53
    avg_press = st.slider("Avg Pressure (Period)", 
                          min_value=29.40, max_value=30.60, value=30.00, step=0.01)

# Prediction logic
if st.button("Predict Power Generation"):
    # Note: Visibility is removed from this list
    input_data = np.array([[
        dist_noon, temp, wind_dir, wind_speed, 
        sky_cover, humidity, avg_wind, avg_press
    ]])
    
    # Scaling and Prediction
    scaled_input = scaler_features.transform(input_data)
    scaled_pred = model.predict(scaled_input)
    actual_pred = scaler_target.inverse_transform(scaled_pred.reshape(-1, 1))
    
    st.metric("Predicted Power Generated", f"{actual_pred[0][0]:.2f} joules")

