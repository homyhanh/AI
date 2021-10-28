import pandas as pd
df0 = pd.read_csv('result0.csv')
df1 = pd.read_csv('result1.csv')
df2 = pd.read_csv('result2.csv')
df3 = pd.read_csv('result3.csv')
df4 = pd.read_csv('result4.csv')
df5 = pd.read_csv('result5.csv')
df6 = pd.read_csv('result6.csv')
df7 = pd.read_csv('result7.csv')
df8 = pd.read_csv('result8.csv')
df9 = pd.read_csv('result9.csv')
df10 = pd.read_csv('result10.csv')
df11 = pd.read_csv('result11.csv')
df12 = pd.read_csv('result12.csv')
# Gộp các số liệu của mỗi testcase thành bảng số liệu chung
data = pd.concat([df0, df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12], ignore_index=True)
data.iloc[:, 1:].to_csv('report.csv') # Chuyển bảng thống kê sang file .csv
print (data.iloc[:, 1:])