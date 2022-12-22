import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from scipy import stats


col1 = "Academic9"
col2 = "StudyTime9"
col3 = "Academic10"
col4 = "StudyTime10"
col5 = "Academic11"
col6 = "StudyTime11"
col7 = "Academic12"
col8 = "StudyTime12"


plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
column9 = [col1, col2]
column10 = [col3, col4]
column11 = [col5, col6]
column12 = [col7, col8]
df = pd.read_csv('C:\\Users\\jerem\\Documents\\input2.csv', usecols=column9)
df2 = pd.read_csv('C:\\Users\\jerem\\Documents\\input2.csv', usecols=column10)
df3 = pd.read_csv('C:\\Users\\jerem\\Documents\\input2.csv', usecols=column11)
df4 = pd.read_csv('C:\\Users\\jerem\\Documents\\input2.csv', usecols=column12)

df1 = df.dropna()
df22 = df2.dropna() 
df33 = df3.dropna()
df44 = df4.dropna()


# print(df1['Academic9'].values.reshape(-1, 1))
# print(df1['StudyTime9'].values.reshape(-1, 1))

x9 = df1['Academic9'].values
y9 = df1['StudyTime9'].values

x10 = df22['Academic10'].values
y10 = df22['StudyTime10'].values

x11 = df33['Academic11'].values
y11 = df33['StudyTime11'].values

x12 = df44['Academic12'].values
y12 = df44['StudyTime12'].values

res9 = stats.linregress(x9, y9)
res10 = stats.linregress(x10, y10)
res11 = stats.linregress(x11, y11)
res12 = stats.linregress(x12, y12)

y91 = (res9.slope*x9) + res9.intercept
y101 = (res10.slope*x10) + res10.intercept
y111 = (res11.slope*x11) + res11.intercept
y121 = (res12.slope*x12) + res12.intercept


plt.plot(x9, y91, color='c')

plt.plot(x10, y101, color='r')

plt.plot(x11, y111, color='m')

plt.plot(x12, y121, color='g')

plt.scatter(df.Academic9, df.StudyTime9, label="Grade 9 - Equation (Rounded to 4 decimals): " + str(round(res9.slope, 4)) + "x + " + str(round(res9.intercept, 4)) + " | R-Value: " + str(round(res9.rvalue, 3)), color='c')
plt.scatter(df2.Academic10, df2.StudyTime10, label="Grade 10 - Equation (Rounded to 4 decimals): " + str(round(res10.slope, 4)) + "x + " + str(round(res10.intercept, 4)) + " | R-Value: " + str(round(res10.rvalue, 3)), color='r')
plt.scatter(df3.Academic11, df3.StudyTime11, label="Grade 11 - Equation (Rounded to 4 decimals): " + str(round(res11.slope, 4)) + "x + " + str(round(res11.intercept, 4)) + " | R-Value: " + str(round(res11.rvalue, 3)), color='m')
plt.scatter(df4.Academic12, df4.StudyTime12, label="Grade 12 - Equation (Rounded to 4 decimals): " + str(round(res12.slope, 4)) + "x + " + str(round(res12.intercept, 4)) + " | R-Value: " + str(round(res12.rvalue, 3)), color='g')
plt.xlabel("Average In Arts Courses")
plt.ylabel("Study Hours Per Day")
plt.legend()
plt.show()