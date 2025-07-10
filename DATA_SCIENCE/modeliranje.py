import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv(r"C:\Users\predr\Downloads\tblTokoviPutnikaZelecnice.csv")
print(df.head())

# x - godine, y - obim H-START
X = df[["Godina"]]
y = df[["Obim H-START"]]

# LINEARNA regresija
model_linear = LinearRegression()  # ✅ Ovde je bila greška
model_linear.fit(X, y)
y_pred_linear = model_linear.predict(X)

#POLINOMSKA regresija
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(X)
poly_model = LinearRegression()
poly_model.fit(x_poly, y)
y_pred_poly = poly_model.predict(x_poly)

#EXPONENCIJALNA regresija
log_y = np.log(y + 1)
exp_model = LinearRegression()
exp_model.fit(X, log_y)
y_pred_log = exp_model.predict(X)
y_pred_exp = np.exp(y_pred_log) - 1

print("Linear:  MSE =", mean_squared_error(y, y_pred_linear), "| R2 =", r2_score(y, y_pred_linear))
print("Polinom: MSE =", mean_squared_error(y, y_pred_poly), "| R2 =", r2_score(y, y_pred_poly))
print("Exponent:    MSE =", mean_squared_error(y, y_pred_exp), "| R2 =", r2_score(y, y_pred_exp))

# 🔮 Prognoza za naredne godine (2020–2024)
godine_buducnost = pd.DataFrame({"Godina": [2020, 2021, 2022, 2023, 2024]})

# Transformišemo podatke za polinomski model (X i X^2)
godine_buducnost_poly = poly.transform(godine_buducnost)

# Pravimo prognoze
prognoze = poly_model.predict(godine_buducnost_poly)

# Ispis rezultata
for godina, vrednost in zip(godine_buducnost["Godina"], prognoze):
    print(f"Prognoza za {godina}: {round(vrednost[0]):,.0f} putnika")

#UPOREDNI GRAFIKONI
plt.plot(X, y, label="Stvarni podaci", marker='o')
plt.plot(X, y_pred_linear, label="Linearni model", linestyle='--')
plt.plot(X, y_pred_poly, label="Polinomski model (2 stepena)", linestyle='--')
plt.plot(X, y_pred_exp, label="Exponencijalni model", linestyle='--')
plt.title("Prognoza obima prev. put. H-START")
plt.xlabel("Godina")
plt.ylabel("Obim H-START")
plt.legend()
plt.grid(True)
plt.show()

# Prikazuj i buduće podatke na istom grafikonu
plt.plot(godine_buducnost, prognoze, label="Prognoza 2020–2024", linestyle=':', marker='x', color='black')
plt.legend()
plt.show()



