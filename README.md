# CrisisResponse

We're Hunter College Computer Science students working on a data science project together through CUNY Tech Prep 2024.

In this team: Tedd Lee, Aaleia Fernando

# Weekly Update:
### OCT 9-15

* [x] Download the data (GW)
* [x] Look at data (all)
* [x] Do some visualization or find out what's messy about it (AF)
* [ ] + bonus ideation
* [x] MVP (GW)

# The Spiel
## Analyzing 911/311 service calls :phone::rotating_light:

* Analyzing the data of service calls based on time of day, location, time of year
* Training a model that predicts the class, type, and needs of an incoming call.
* (Further Study) How do other environmental factors affect the many different crises faced in NYC?

### Why? 
This model could potentially help first responders and call operators, if we get an idea of what to expect from a call based on location and time, we can deploy the appropriate services even quicker, or ensure we have enough resources to deal with an expected influx of certain calls. Furthermore, we want to explore if there is data to support statements relating weather and environmental factors to issues such as crime. For example, it is commonly stated that the summer heat leads to an increase in crime rates, or if poor weather correlates with less crime and more accidents. While correlation != causation, it would be interesting to see if such statements are substantiated by the data.

### Team member responsibilities:
* Tedd:
  * Data organization, visualization, and analysis.
  * Flexible role, can help out wherever needed.
* Aaleia:
  * Data preprocessing
  * Feature engineering, hyperparameter tuning, etc.
  * Frontend build (TBD)
  * Outlines & insights

### The Data
* [911 calls](https://data.cityofnewyork.us/Public-Safety/NYPD-Calls-for-Service-Year-to-Date-/n2zq-pubd/about_data)
* [311 calls](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9/about_data)

### Video tutorials we think would help:
* [Building a Neural Network with PyTorch](https://www.youtube.com/watch?v=mozBidd58VQ) (Georgina)
* [How to Build a Data Pipeline](https://youtu.be/hKv70zftW-Y?si=CpZzFRkK_2CEemNN) (Tedd)
* [End To End Machine Learning | Classification & Regression](https://www.youtube.com/watch?v=ocse1X_rtSI) (Aaleia)

## MVP
The minimum viable product for this would be a data visualization project of the various crises in NYC over the past years. We can display the top crises by location, time of day, year, and combine that visualization with data of weather and location specific factors at the same time.

The goal for the full project is to develop a classification model that decides what type of crisis an incoming call may be about, and what kind of emergency or non emergency services will be required.

## Schedule/Task Outline:
### Data cleaning and preprocessing
* [ ] Hunt down datasets that are directly related to our project ideas
* [ ] Find additional datasets that might be useful or add useful insights to our analysis
* [ ] Get familiar with how the raw data might break things.

### Data analysis
* [ ] Initial glances at trends and outliers
* [ ] Data visualization

### Feature selection
* [ ] Identify features to be used in training our model
### Model building
### Model evaluation
### Presenting our findings
