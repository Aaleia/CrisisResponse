import numpy as np
import pandas as pd
from catboost import CatBoostClassifier, Pool

model = CatBoostClassifier()
model.load_model('model_v0')

target_col = 'FINAL_CALL_TYPE'
feature_cols = ['INITIAL_CALL_TYPE', 'INITIAL_SEVERITY_LEVEL_CODE', 'DAY_OF_WEEK', 'INCIDENT_HOUR', 'INCIDENT_DURATION', 'POLICEPRECINCT', 'ZIPCODE']
categorical_features = ['INITIAL_CALL_TYPE', 'DAY_OF_WEEK', 'POLICEPRECINCT', 'ZIPCODE']

def encode(data):
	params = data.copy()

	params['INCIDENT_DATETIME'] = pd.to_datetime(params['INCIDENT_DATETIME'])
	params['INCIDENT_CLOSE_DATETIME'] = pd.to_datetime(params['INCIDENT_CLOSE_DATETIME'])

	params['DAY_OF_WEEK'] = params['INCIDENT_DATETIME'].dayofweek
	params['INCIDENT_HOUR'] = params['INCIDENT_DATETIME'].hour
	params['INCIDENT_DURATION'] = (params['INCIDENT_CLOSE_DATETIME'] - params['INCIDENT_DATETIME']).total_seconds()
	params['POLICEPRECINCT'] = params['POLICEPRECINCT'].astype(str)
	params['ZIPCODE'] = params['ZIPCODE'].astype(str)

	return params[feature_cols]


def predict(params):
	try:
		print(params)
		res = model.predict(params)

		return res[0]
	except Exception as e:
		print(e)
		return "error"