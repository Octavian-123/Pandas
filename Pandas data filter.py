
import pandas as pd

df = pd.read_csv("ESPT4A data.csv")

filtered = df[(df["Property Type"] == "Bungalow") & (df["Rooms"] == 3)]

print(filtered [["Region Code", "Region", "Property Type", "Rooms"]])
