import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_sales(df):
    products = df['product'].unique()

    for product in products:
        temp = df[df['product'] == product]

        plt.figure(figsize=(12,6))

        plt.plot(temp['date'], temp['sales'], label='Actual')
        plt.plot(temp['date'], temp['predicted_sales'], label='Predicted')

        plt.title(f"Sales Forecast - {product}")
        plt.xlabel("Date")
        plt.ylabel("Sales")

        # 🔥 PROFESSIONAL FIX
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())   # show months only
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))  # Jan, Feb...

        plt.xticks(rotation=45)
        plt.legend()

        plt.tight_layout()

        plt.savefig(f"images/{product}_forecast.png")
        plt.close()