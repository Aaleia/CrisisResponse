import streamlit as st
import numpy as np
import pandas as pd

from model import predict, encode

if 'sample_data' not in st.session_state:
	data = pd.read_csv('week_in_march.csv')
	data.dropna(inplace=True)
	st.session_state.sample_data = data.sample(100).reset_index()

sample_data = st.session_state.sample_data

st.title('EMS Call Type Prediction Model')

st.header('Sample Data from a Week in March 2024')
st.dataframe(sample_data, use_container_width=True)

selected = st.slider("Choose a row:", 0, sample_data.shape[0], 0)

if 'selected' not in st.session_state or st.session_state.selected != selected:
	row = encode(sample_data.iloc[selected])
	predicted_label = predict(row)

	st.session_state.selected = selected

st.write(predicted_label)