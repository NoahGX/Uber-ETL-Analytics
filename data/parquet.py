import pandas as pd

# Read the Parquet file
df = pd.read_parquet("file-name.parquet")

# Convert and save as CSV
df.to_csv("uber_data.csv", index=False)
print("Conversion complete: uber_data.csv")