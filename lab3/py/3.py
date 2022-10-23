import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1
df = pd.read_csv("la-crimes-sample.csv")

# 2
print(f"2.\nrows: {len(df.index)}, cols: {len(df.columns)}")

# 3
print("\n3.")
df.info()

# 4
print("\n4.")
print(df.nunique())

# 5
print("\n5.")
print(df.isna().sum())

# 6
print("\n6.")
counts_female = (df["Victim Sex"] == "F").value_counts()
counts_male = (df["Victim Sex"] == "M").value_counts()

print(f"female victims: {counts_female[0]}\nmale victims: {counts_male[0]}")
if counts_female[0] > counts_male[0]:
    print("true")
else:
    print("false")

# 7
print("\n7.")
crimes = df["Crime Code"].value_counts()
print(crimes[:10])
plt.bar(list(map(str, crimes[:10].index)), crimes[:10].values)
plt.xlabel("crime code")
plt.ylabel("offense count")
plt.savefig("crimes.png")

# 8
print("\n8.")
counts_female = df[df["Victim Sex"] == "F"]["Crime Code"].value_counts()
counts_male = df[df["Victim Sex"] == "M"]["Crime Code"].value_counts()
print("female: ", df[df["Crime Code"] == counts_female.index[0]]["Crime Code Description"].values[0])
print("male: ", df[df["Crime Code"] == counts_male.index[0]]["Crime Code Description"].values[0])

# 9
print("\n9.")
print(df["Victim Descent"].value_counts()[:3])

# 10
print("\n10.")
areas = df["Area Name"].value_counts()
safe_n, safe_v = areas.index[-1], areas.values[-1]
dang_n, dang_v = areas.index[0], areas.values[0]
plt.figure()
plt.bar([safe_n, dang_n], [safe_v, dang_v])
plt.savefig("regions.png")
