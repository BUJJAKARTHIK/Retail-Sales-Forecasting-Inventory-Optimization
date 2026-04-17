def create_features(df):
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['weekday'] = df['date'].dt.weekday

    # Convert product to numeric
    df['product_id'] = df['product'].astype('category').cat.codes

    return df