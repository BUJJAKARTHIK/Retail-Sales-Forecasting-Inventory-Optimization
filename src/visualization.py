import matplotlib.pyplot as plt

def plot_sales(df):
    products = df['product'].unique()

    for product in products:
        temp = df[df['product'] == product]

        plt.figure()
        plt.plot(temp['date'], temp['sales'], label='Actual')
        plt.plot(temp['date'], temp['predicted_sales'], label='Predicted')
        plt.title(f"Sales Forecast - {product}")
        plt.legend()
        plt.savefig(f"images/{product}_forecast.png")