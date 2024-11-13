# CrisisResponse

We're Hunter College Computer Science students working on a data science project together through CUNY Tech Prep 2024.
View weekly updates [below](#weekly-updates).

In this team: Tedd Lee, Aaleia Fernando

# The Spiel
## Analyzing EMS Computer Aided Dispatch System Data from the FDNY :phone::rotating_light:
* EMS personel respond to a wide variety of calls, including both physical and mental health emergencies. Our project aims to improve the accuracy of determining NYC EMS call type before completion of the call, with the ultimate purpose of improving the actual response to such emergencies by ensuring the right personell and resources are made available on-site as soon as possible. Currently, there is about 90% accuracy in determining call type when a call is first placed -- we believe that we can do better.

### Team member responsibilities:
* Tedd:
  * Data organization
  * Visualization and analysis
  * Backend development
* Aaleia:
  * Data preprocessing
  * Feature engineering, hyperparameter tuning
  * Frontend build

### The Data
* [Dispatch calls](https://data.cityofnewyork.us/Public-Safety/EMS-Incident-Dispatch-Data/76xm-jjuj/about_data)
* [Weather data (hourly)](https://open-meteo.com/en/docs/historical-weather-api#latitude=40.71&longitude=-74.01&start_date=2023-01-01&end_date=2024-10-30&hourly=temperature_2m,precipitation,rain,snowfall,snow_depth,wind_speed_10m,wind_gusts_10m&daily=&timezone=America%2FNew_York)

### Video tutorials we think would help:
* [How to Build a Data Pipeline](https://youtu.be/hKv70zftW-Y?si=CpZzFRkK_2CEemNN) (Tedd)
* [End To End Machine Learning | Classification & Regression](https://www.youtube.com/watch?v=ocse1X_rtSI) (Aaleia)

## MVP
* A supervised model with >90% accuracy predicting final call emergency type.
* A simple frontend application allowing user input and an output of predicted label.
* At least one major visualization of an insight we gained from exploring and analyzing the data.

## Schedule/Task Outline:

### Data cleaning and preprocessing
* [ ] Hunt down datasets that are directly related to our project ideas
* [ ] Find additional datasets that might be useful or add useful insights to our analysis
* [ ] Get familiar with how the raw data might break things.

### Data analysis
* [ ] Initial glances at trends and outliers
* [ ] Data visualization focusing on specific potential insights
* [ ] Identify features to be used in training our model

### Model building
* [ ] Start with barebones random forest
* [ ] Adjust features used and hyperparameters to achieve higher accuracy
* [ ] Add additional features from external data sources (e.g. weather and/or special event data)
* [ ] Evaluation and optimization

### Presenting our findings
* [ ] Develop simple webapp to display our results
* [ ] Connect model and allow for user input and model predictions
* [ ] Add final insights and visualizations to the site
* [ ] Develop a final presentation

# Weekly Updates:

### NOV 6
* [x] Initial random forest model complete
* [ ] Optimize for higher accuracy (try using gradient-boosting) (T)
* [ ] Incorporate new data (start with weather data) (A)
* [ ] Ideation for frontend build

### OCT 30
* [x] outline the rest of the project MVP, weekly goals, project direction
* [ ] analyze data and create visualizations
* [ ] group classifications
* [x] one-hot encoding
* [x] build initial model

### OCT 23
* [x] Regrouping - find new dataset and new MVP

### OCT 16
* [x] Completed data understanding and exploration
* [x] Completed initial model build (A)

### OCT 9
* [x] Download the data
* [x] Initial visualization (AF)
* [x] + bonus ideation
* [x] Determine MVP
