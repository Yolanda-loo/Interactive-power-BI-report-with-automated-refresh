import pandas as pd
import datetime

# Step 1: Load raw dataset
df = pd.read_csv("data/business_kpi_sample_data.csv")

# Step 2: Apply transformations
df["Profit"] = df["Revenue"] - df["Expenses"]
df["CAC"] = df["Expenses"] / df["Customers"]

# Add a refresh timestamp
refresh_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
df["Last_Refresh"] = refresh_time

# Step 3: Save refreshed dataset
output_file = "data/business_kpi_refreshed.csv"
df.to_csv(output_file, index=False)

print(f"Dataset refreshed and saved to {output_file} at {refresh_time}")
