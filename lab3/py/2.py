import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = [["Вжик", "Zipper the Fly", "fly", "0.7"],
["Гайка", "Gadget Hackwrench", "mouse", None],
["Дейл", "Dale", "chipmunk", "1"],
["Рокфор", "Monterey Jack", "mouse", "0.8"],
["Чип", "Chip", "chipmunk", "0.2"]]

# 1
df = pd.DataFrame(data, columns=["ru_name", "en_name", "class", "cheer"])
df["cheer"] = df["cheer"].apply(lambda x: pd.to_numeric(x))
print("1.")
print(df)
df.info()

# 2
print("\n2.")
print(f"n of rows: {len(df.index)}")

# 3
print("\n3.")
print(f"non-na in [cheer]: {df['cheer'].notna().sum()}")

# 4
print(f"\n4.\ndf[3][2]: {df.iloc[2][1]}")

# 5
print("\n5.")
df1 = df[1:4]
print(df1)

# 6
# Done in #1

# 7
print("\n7.")
df["logcheer"] = df["cheer"].apply(np.log)
print(df)

# 8
print("\n8.")
counts = df["class"].value_counts()
print(counts)
plt.bar(counts.index, counts.values)
plt.title("classes")
plt.xlabel("class")
plt.ylabel("count")
plt.savefig("classes.png")