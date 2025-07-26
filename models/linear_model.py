from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

def train_linear_model(x, y):
    model = LinearRegression()
    model.fit(x, y)
    
    return model
def evaluate_model(model, x, y):
    y_pred = model.predict(x)
    mse = mean_absolute_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    
    return y_pred, mse, r2