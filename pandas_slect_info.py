
import pandas as pd

data = pd.read_csv("winter_olympics.csv")

# Filter for USA athletes under 22
filtered = data[(data["country"] == "USA") & (data["age"] < 22)]

# Sort by age (Ascending)
sorted_result = filtered.sort_values(by = "age", ascending = True)

# Select wanted columns
result = sorted_result[["athlete", "sport", "medal"]]

print(result)
