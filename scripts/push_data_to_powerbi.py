import requests
import time
import pandas as pd

# Your Power BI streaming dataset endpoint
url = "https://api.powerbi.com/beta/your_workspace_id/datasets/your_dataset_id/rows?key=your_push_key"

# Load sample data
df = pd.read_csv("../data/sample_sales_data.csv")

# Simulate real-time stream
for index, row in df.iterrows():
    payload = [{
        "Date": row["Date"],
        "Region": row["Region"],
        "Sales_Amount": row["Sales_Amount"],
        "New_Customers": row["New_Customers"],
        "Channel": row["Channel"]
    }]
    
    r = requests.post(url, json=payload)
    
    if r.status_code == 200:
        print(f"✅ Pushed row {index + 1}")
    else:
        print(f"❌ Failed to push row {index + 1}: {r.text}")
    
    time.sleep(5)  # Wait 5 seconds between each push
