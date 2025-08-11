from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

def train_linear_model(x, y):
    train_model1 = LinearRegression()
    train_model1.fit(x, y)
    
    return train_model1

def evaluate_train_linear_model(model: LinearRegression, x, y):
    y_predict = model.predict(x)
    mae = mean_absolute_error(y, y_predict)
    r2 = r2_score(y, y_predict)
    
    return y_predict, mae, r2

#Funkcije za predikciju (prognozu) je završena.. PecaPixel :D