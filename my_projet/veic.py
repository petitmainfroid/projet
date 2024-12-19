import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Ols import OrdinaryLeastSquares





data = pd.read_csv(r'vehicles.csv',encoding='latin-1',
                   on_bad_lines='skip')

#X = pd.get_dummies(data.drop(columns=['CO2 emissions (g/km)']), drop_first=True)
data_encoded = pd.get_dummies(data.drop(columns=['CO2 emissions (g/km)', 'Model']),
                              drop_first=True)
y = data['CO2 emissions (g/km)']

model_target_mean = data.groupby('Model')['CO2 emissions (g/km)'].mean()
data['Model_Target'] = data['Model'].map(model_target_mean)
data_encoded['Model_Target'] = data['Model'].map(model_target_mean)

#X['Model_freq'] = frequency_encoding(data, 'Model')


# vérifier il n'y a pas valeur vide
X = data_encoded.fillna(0)
y = y.fillna(0)

model = OrdinaryLeastSquares(intercept=False)
res=model.fit(X, y)

# Predict
y_pred = model.predict(X)

y1=y.values.reshape(-1, 1)
model.visualize_results(y1, y_pred)
print("R^2的值",model.determination_coefficient(X,y1))
print("MSE",model.mean_squared_error(X, y))