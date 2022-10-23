import pandas as pd


# 1
s1 = pd.Series(data=[i for i in range(1, 6)], index=['a', 'b', 'c', 'd', 'e'])
print("1.", s1)

# 2
print("\n2.", s1['d'], sep="\n")

# 3
print("\n3.", s1[1], sep="\n")

# 4
s1['f'] = 6
print("\n4.", s1, sep="\n")

# 5
print("\n5.", s1['c':'e'], sep="\n")

# 6
df = pd.DataFrame([[1, 2], [5, 3], [3.7, 4.8]], columns=['col1', 'col2'])
print("\n6.", df, sep="\n")

# 7
print("\n7.", df['col1'][2], sep="\n")

# 8
df[df == 3] = 9
print("\n8.", df, sep="\n")

# 9
print("\n9.", df[1:3], sep="\n")

# 10
df['col3'] = df['col1'] * df['col2']
print("\n10.", df, sep="\n")