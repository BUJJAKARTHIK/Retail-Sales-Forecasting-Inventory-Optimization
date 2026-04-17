from sklearn.ensemble import RandomForestRegressor

def train_model(df):
    X = df[['day','month','weekday','product_id']]
    y = df['sales']
    
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)
    
    return model

def predict(model, df):
    X = df[['day','month','weekday','product_id']]
    return model.predict(X)