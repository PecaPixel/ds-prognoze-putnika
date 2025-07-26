import pandas as pd
import numpy as np
from models.linear_model import train_linear_model, evaluate_model
from models.exp_model import train_exp_model, evaluate_exp_model

df = pd.read_csv("data/tblTokoviPutnikaZelecnice.csv")
print("============================================================================")
print("Kolone u fajlu: ")
print(df.columns)
print("============================================================================")

#Priprema podataka u smislu odabira potrebnih kolona
X = df[["Godina"]] #ovo uzimam da mi je kolona Godina X promenjiva i ona u ovom slucaju ima 11 redova tj 11 godina
y = df["Obim H-START"]

#Treniranje modela
prvi_model = train_linear_model(X, y)

#Evaluacija modela
y_pred, mse, r2 = evaluate_model(prvi_model, X, y)

 #Ispis rezultata
print("\nRezultati modela: ")
print(f"   -MSE: {mse:.2f}")
print(f"   -R2: {r2: .4f}")

#Predikcija za novu godinu
unos = input("Unesi godine za koje želiš predikciju: ")
godine_za_predikciju = [[int(godina.strip())] for godina in unos.split(",")]
nova_godina = pd.DataFrame(godine_za_predikciju, columns=["Godina"])
predikcija= prvi_model.predict(nova_godina)
print("============================================================================")
for godina, vrednost in zip(nova_godina["Godina"], predikcija):
    print(f"Predviđanje za {godina}: {int(vrednost)} putnika")
print("============================================================================")

#Treniranje modela Exp
model2 = train_exp_model(X, y)

#Evaluacija Exp modela
y_exp_pred, mae_exp, r2_exp = evaluate_exp_model(model2, X, y)

#Ispis rezultata
print("\nRezultati Exp modela: ")
print(f"    MAE: {mae_exp: .2f}")
print(f"    R2: {r2_exp: .4f}")

#Predikcija za nove kodine pomoću Exponencijalnog moela
exp_predikcija_log = model2.predict(nova_godina)
exp_predikcija = np.exp(exp_predikcija_log)
print("============================================================================")
print("Predikcije eksp. modela za nove godine:")
for godina, vrednost in zip(nova_godina["Godina"], exp_predikcija):
    print(f"Exp predviđanje za {godina}: {int(vrednost)} putnika")
print("============================================================================")
