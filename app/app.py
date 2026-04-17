import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Retail Sales Forecasting & Inventory Optimization")

# Load data
forecast = pd.read_csv("outputs/forecast.csv")
inventory = pd.read_csv("outputs/inventory.csv")

# Convert date
forecast['date'] = pd.to_datetime(forecast['date'])

# Sidebar filter
product = st.sidebar.selectbox("Select Product", forecast['product'].unique())

filtered = forecast[forecast['product'] == product]

# Plot
st.subheader(f"Sales Forecast for {product}")

fig, ax = plt.subplots()
ax.plot(filtered['date'], filtered['sales'], label="Actual")
ax.plot(filtered['date'], filtered['predicted_sales'], label="Predicted")
ax.legend()

st.pyplot(fig)

# Inventory Table
st.subheader("📦 Inventory Optimization")

st.dataframe(inventory)

# Highlight reorder alert
st.subheader("⚠ Reorder Alerts")

alerts = inventory[inventory['reorder_point'] > inventory['avg_demand'] * 5]

st.dataframe(alerts)