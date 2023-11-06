import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("train.csv")

df = df.drop_duplicates()

correlation_coef = df["age"].corr(df["limit_bal"])
print(f"\nAge and limit correlation coeficient: {correlation_coef}")


bills_col = ['bill_amt1', 'bill_amt2', 'bill_amt3', 'bill_amt4', 'bill_amt5', 'bill_amt6']

df['sum'] = df[bills_col].sum(axis=1)
print(df)

print(df.sort_values(by='age', ascending=False).head(10)[['limit_bal', 'age', 'education:0', 'education:1',
                                                          'education:2', 'education:3', 'education:4', 'education:5',
                                                          'education:6', 'sum']])

plt.subplot(2, 2, 1)
plt.hist(df['limit_bal'])

plt.subplot(2, 2, 2)
plt.hist(df['age'])

plt.subplot(2,1,2)
plt.plot(df['age'], df['limit_bal'], "r.")
plt.show()

