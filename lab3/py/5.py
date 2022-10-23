import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("vgsales.csv")

# 1
print(df["Platform"].unique())

# 2
df_m = pd.read_csv("metacritic_games.csv")
df_merged = pd.merge(df, df_m, on=["Name"], how="inner")
print(df_merged)
df["metacritic_rating"] = df_merged["rating"]
print(df)

# 3
games_2012 = df[(df["metacritic_rating"] == "M") & (df["Year"] >= 2012)]
print(games_2012)

# 4
print(games_2012.describe())

# 5
def check_vowels(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for v in vowels:
        if v in x:
            count += 1
    if count >= 3:
        return True
    return False
        
genres = df[df["Genre"].apply(check_vowels)]
res = {}
for genre in genres["Genre"].unique():
    g = genres[genres["Genre"] == genre]
    res[genre] = g['Name'].count()

print(res)