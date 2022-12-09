import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

df = pd.read_csv('HR_comma_sep.csv')

left = df[df.left == 1]
retained = df[df.left == 0]

pd.set_option('display.max_columns', None)

pd.crosstab(df.salary, df.left).plot(kind='bar')
pd.crosstab(df.Department, df.left).plot(kind='bar')
plt.show()

df_sub = df[['satisfaction_level', 'average_montly_hours', 'promotion_last_5years', 'salary']]
print(df_sub.head())

salary_dummies = pd.get_dummies(df_sub.salary, prefix='salary')
df_with_dummies = pd.concat([df_sub, salary_dummies], axis='columns')
df_with_dummies.drop('salary', axis='columns', inplace=True)

X = df_with_dummies
y = df.left

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.4)

model = LogisticRegression()
model.fit(X_train, y_train)

print(model.predict(X_test))
print(model.score(X_test, y_test))




