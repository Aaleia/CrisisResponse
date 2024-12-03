import numpy as np
import pandas as pd
from catboost import CatBoostClassifier, Pool

model = CatBoostClassifier()
model.load_model('model_v0')

target_col = 'FINAL_CALL_TYPE'
feature_cols = ['INITIAL_CALL_TYPE', 'INITIAL_SEVERITY_LEVEL_CODE', 'day_of_week', 'incident_hour', 'incident_duration', 'POLICEPRECINCT', 'ZIPCODE']
categorical_features = ['INITIAL_CALL_TYPE', 'day_of_week', 'POLICEPRECINCT', 'ZIPCODE']

def encode(data):
	params = data.copy()

	params['INCIDENT_DATETIME'] = pd.to_datetime(params['INCIDENT_DATETIME'])
	params['INCIDENT_CLOSE_DATETIME'] = pd.to_datetime(params['INCIDENT_CLOSE_DATETIME'])

	params['day_of_week'] = params['INCIDENT_DATETIME'].dayofweek
	params['incident_hour'] = params['INCIDENT_DATETIME'].hour
	params['incident_duration'] = (params['INCIDENT_CLOSE_DATETIME'] - params['INCIDENT_DATETIME']).total_seconds()
	params['POLICEPRECINCT'] = params['POLICEPRECINCT'].astype(str)
	params['ZIPCODE'] = params['ZIPCODE'].astype(str)

	return params[feature_cols]


def predict(params):
	try:
		res = model.predict(params)

		return res[0]
	except Exception as e:
		print(e)
		return "error"