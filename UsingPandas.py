import pandas as pd
df1 = pd.read_excel("MOCK_DATA_1.xlsx", engine='openpyxl')
df2 = pd.read_excel("MOCK_DATA_2.xlsx", engine='openpyxl')
df3 = pd.read_excel("MOCK_DATA_3.xlsx", engine='openpyxl')

print(df1)
print("\n\n\n")
print(df2)
print("\n\n\n")
print(df3)
print("\n\n\n")

df_concat = pd.concat([df1, df2])
print(df_concat)
print("\n\n\n")

df_merge = pd.merge(df_concat, df3, on='specialization')
df_merge.drop('gender', axis=1, inplace=True)

print(df_merge)