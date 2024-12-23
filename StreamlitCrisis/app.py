import streamlit as st
import numpy as np
import pandas as pd
import time

from model import predict, encode

if 'sample_data' not in st.session_state:
	data = pd.read_csv('week_in_march.csv')
	data.dropna(inplace=True)
	st.session_state.sample_data = data.sample(100).reset_index()

sample_data = st.session_state.sample_data

st.title('EMS Call Classifier')
st.write("This project aims to improve the accuracy of predicting the nature of emergency calls in NYC, thereby improving emergency response times. It utilizes historical EMS dispatch data and real-time weather conditions to predict call types. The project's ultimate goal is to get New Yorkers the help they need even faster.")

st.header('The Data')
st.write('Provided through the NYC Open Data.')
t1, t2 = st.tabs(['EMS Incident Dispatch', 'Weather'])
t1.markdown(
"""The [EMS Incident Dispatch Data](https://data.cityofnewyork.us/Public-Safety/EMS-Incident-Dispatch-Data/76xm-jjuj/about_data) is generated by the EMS Computer Aided Dispatch System, and covers information about the incident as it relates to the assignment of resources and the Fire Department’s response to the emergency.

The 6GB of data spans from April 2008 to October 2024 and employs the use of over 140 distinct call types (e.g. “Eye Injury” or “Cardiac Arrest”).
""")


t2.write("The Weather Data comes from...")


t1.subheader('Sample of 100 Incidents from March 2024')
t1.dataframe(sample_data, use_container_width=True)

st.header("Analysis")
st.write("At least one major visualization of an insight we gained from exploring and analyzing the data.")


st.header("Our Model")

st.markdown(
"""
Our model utilizes a Random Forest Multiclassifier enhanced with Gradient Boosting. We selected key features like time of day, day of week, borough, police precinct, and zip code, which proved most relevant in predicting the nature of an EMS dispatch incident. Initial call type and initial severity level were also included to provide a baseline for our predictions.
"""	
)

st.subheader("Demo")

selected = st.slider("Choose a row:", 0, sample_data.shape[0]-1, 0)

if 'selected' not in st.session_state or st.session_state.selected != selected:
	row = encode(sample_data.iloc[selected])
	correct_label = sample_data.loc[selected, "FINAL_CALL_TYPE"]

	c1, c2 = st.columns(2)
	c1.dataframe(row)
	c2.write("Correct Type:")
	c2.dataframe({"FINAL_CALL_TYPE": correct_label})
	
	t1 = time.time()*1000
	predicted_label = predict(row)
	t2 = time.time()*1000
	c2.write("Predicted Type:")
	c2.dataframe({"PREDICTED_CALL_TYPE": predicted_label})

	if correct_label == predicted_label:
		st.success(f"""Label successfully predicted in {t2-t1:.2f}ms!""")
	else:
		st.info(f"""The predicted label did not match the correct final label. We acknowledge that our model is unable to accurately predict the current label in all possible cases.""")
	
	st.session_state.selected = selected


st.header("Results")
st.markdown(
"""
We achieved 89% accuracy on the largest subset of data we were able to train on - this is a 4% increase in accuracy from the preexisting typing system.

This includes 83% accuracy in typing calls initially marked as “Unknown.”

Incorporating any weather data besides temperature typically led to overfitting and decreased accuracy by up to 10%.
However, including snowfall data boosted accuracy by 2% when using a subset of just winter months.
"""
)
