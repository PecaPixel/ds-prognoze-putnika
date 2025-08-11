from models.linear_model import train_linear_model, evaluate_train_linear_model
import pandas as pd
import numpy as np
import math

df = pd.read_csv("data/tblTokoviPutnikaZelecnice.csv")
print("===================učitavanje tabele i pregled imena svih kolona=====================")
print(df.columns)
print("=====================================================================================")

#Priprema podataka za upotrebu
X = df[["Godina"]]
y = df["Obim H-START"]
#Učenje modela sa konkretnim podacima
model_1 = train_linear_model(X, y)
#Ocena modela na konkretnim podacima Obim H-START za postojeće godine
y_pred_model_1, mae, r2 = evaluate_train_linear_model(model_1, X, y)
print(f"Srenja apsolutna greška iznosi = {math.ceil(mae):,}")
print(f"Koeficijent korelacije iznosi = {r2:.4f}")
print("====================Ocena kvaliteta modela===========================================")
if 0 <= r2 < 0.50:
    print(f"r2 je {r2:.4f} u granicam 0 <= r2 < 0.50. To znači da je loš za prognozu (potraži bolji model!)")
elif 0.50 <= r2 < 0.75:
    print("Model je osrednji. Postoji prostora za poboljšanje!")
elif 0.75 <= r2 < 0.90:
    print("Model je dobar za prognozu!")
elif 0.90 <= r2 < 1:
    print("Model je izuzetno dobar!")
print("=====================================================================================")
print("Prognoza za buduće unete godine na osnovu naučenog modela X - godine i y - obim prevoza")
unos = input("Unesi nove buduće godine za prognozu (npr. 2020, 2021, 2022 itd: )")
nove_godine_1 = [int(godine.strip()) for godine in unos.split(",")]
print(f"Unede godine za prognozu su: {nove_godine_1}")
x_nove = pd.DataFrame(nove_godine_1, columns=["Godina"])
y_predict_nove_god = model_1.predict(x_nove)
y_pred_nove_ceil = np.ceil(y_predict_nove_god).astype(int)
#Kreiranje novog data frejma za prognozirane godine
df_prognozirano = pd.DataFrame({"Godina": nove_godine_1, "Prognozirane vrednosti": y_pred_nove_ceil})

print("====================Prognoza za unete godine=========================================")
print(df_prognozirano.to_string(index=False))
print("=====================================================================================")