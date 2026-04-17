import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)

    dates = pd.date_range(start="2023-01-01", end="2023-12-31")
    products = ['Milk', 'Bread', 'Rice', 'Eggs']

    data = []

    for product in products:
        base_sales = np.random.randint(20, 50)

        for date in dates:
            # Trend (increase over time)
            trend = (date.dayofyear) * 0.05

            # Seasonality (weekly pattern)
            if date.weekday() >= 5:  # weekend
                seasonal = 10
            else:
                seasonal = 0

            # Random noise
            noise = np.random.normal(0, 5)

            sales = max(0, int(base_sales + trend + seasonal + noise))

            data.append([date, product, sales])

    df = pd.DataFrame(data, columns=['date', 'product', 'sales'])
    df.to_csv("data/raw/sales.csv", index=False)

    print("✅ Dataset generated successfully!")

if __name__ == "__main__":
    generate_data()