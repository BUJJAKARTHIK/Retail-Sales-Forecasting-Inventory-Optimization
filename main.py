from src.data_preprocessing import load_data
from src.feature_engineering import create_features
from src.model import train_model, predict
from src.inventory import inventory_optimization
from src.visualization import plot_sales

# Load data
df = load_data("data/raw/sales.csv")

# Feature engineering
df = create_features(df)

# Train model
model = train_model(df)

# Predictions
df['predicted_sales'] = predict(model, df)

# Inventory optimization
inventory_df = inventory_optimization(df)

# Save outputs
df.to_csv("outputs/forecast.csv", index=False)
inventory_df.to_csv("outputs/inventory.csv", index=False)

# Plot graph
plot_sales(df)

print("✅ Project executed successfully!")