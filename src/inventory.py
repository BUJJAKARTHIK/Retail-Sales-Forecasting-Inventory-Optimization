def inventory_optimization(df):
    result = []

    products = df['product'].unique()

    for product in products:
        temp = df[df['product'] == product]

        avg_demand = temp['predicted_sales'].mean()
        std_demand = temp['sales'].std()

        lead_time = 7  # days

        safety_stock = std_demand * 1.65
        reorder_point = (avg_demand * lead_time) + safety_stock

        result.append([product, avg_demand, safety_stock, reorder_point])

    import pandas as pd
    return pd.DataFrame(result, columns=[
        'product','avg_demand','safety_stock','reorder_point'
    ])