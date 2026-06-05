import pandas as pd
from datetime import datetime

def refresh_data(input_file: str, output_file: str):
    # Load raw dataset
    df = pd.read_csv(input_file)

    # Example KPI transformations (customize for your business logic)
    df['Revenue_per_Product'] = df['Revenue'] / df['Units_Sold']
    df['Expense_Ratio'] = df['Expenses'] / df['Revenue']

    # Add refresh timestamp
    df['last_refresh_timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save refreshed dataset
    df.to_csv(output_file, index=False)
    print(f"Data refreshed and saved to {output_file}")

if __name__ == "__main__":
    input_path = "data/business_kpi_sample_data.csv"
    output_path = "data/business_kpi_refreshed.csv"
    refresh_data(input_path, output_path)
