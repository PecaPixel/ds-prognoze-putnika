import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv(r"C:\Users\predr\Downloads\tblTokoviPutnikaZelecnice.csv")
print("==================================================================")
print(df.head)
print("==================================================================")
X = df[["Godina"]]  
y = df[["Obim H-START"]]

#LINEARNA regresija
model_linear = LinearRegression()
model_linear.fit(X, y)
y_pred_linear = model_linear.predict(X)
print("Linear   MSE: ", mean_squared_error(y, y_pred_linear), "| R2: ", r2_score(y, y_pred_linear))

#EXPONENCIJALNA regresija
log_y = np.log(y + 1)
exp_model = LinearRegression()
exp_model.fit(X, log_y)
y_pred_log = exp_model.predict(X)
y_pred_exp = np.exp(y_pred_log) - 1
print("Exp      MSE: ", mean_squared_error(y, y_pred_exp), "| R2: ", r2_score(y, y_pred_exp))

#POLINOMSKA regresija
poly = PolynomialFeatures(degree=50)
x_poly = poly.fit_transform(X)
poly_model = LinearRegression()
poly_model.fit(x_poly, y)
y_pred_poly = poly_model.predict(x_poly)
print("Ply       MSE: ", mean_squared_error(y, y_pred_poly), "| R2: ", r2_score(y, y_pred_poly))

#RANDOM Forest Regresion
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X, y.values.ravel())
y_pred_rf = rf_model.predict(X)
print("R.F.      MSE: ", mean_squared_error(y, y_pred_rf), "| R2: ", r2_score(y, y_pred_rf))

plt.plot(X, y, label="Stvarni podaci", marker='o')
plt.plot(X, y_pred_rf, label="Random Forest", linestyle='--')
plt.title("Uporedni grafikon: Random Forest vs stvarni podaci")
plt.xlabel("Godina")
plt.ylabel("Obim H-START")
plt.legend()
plt.grid(True)
plt.show()

