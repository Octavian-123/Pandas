
import pandas as pd

df = pd.read_csv("ESPT4A data.csv")

filtered = df[(df["Property Type"].isin(["Bungalow","Semi-Detached","Detached"])) & (df["Rooms"] >= 2)]

srt = input("What do you want to sort by?")

sorted_df = filtered.sort_values(by = srt, ascending = True)

print(sorted_df[["Region Code", "Region", "Property Type", "Rooms"]])
