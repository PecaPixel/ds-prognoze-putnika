import pandas as ps
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np

def train_exp_model(a, b):
    y_log = np.log(b + 1)
    modelExp = LinearRegression()
    modelExp.fit(a, y_log)
    
    return modelExp

def evaluate_exp_model(model, a, b):
    y_log_predict = model.predict(a)
    y_predict = np.exp(y_log_predict) - 1
    mae = mean_absolute_error(b, y_predict)
    r2 = r2_score(b, y_predict)
    
    return y_predict, mae, r2
    