import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('LogR_insurance.csv')

plt.scatter(df.age, df.bought_insurance, marker='+', color='red')
plt.xlabel('age')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(df[['age']], df.bought_insurance, test_size=0.1)


model = LogisticRegression()
model.fit(X_train, y_train)

print(f'Test sample: {X_test}')
print(f'Model prediction: {model.predict(X_test)}')
print(f'Model probabilities: {model.predict_proba(X_test)}')
print(f'Model score: {model.score(X_test, y_test)}')
i = 29
print(f'Prediction for i = {i}: {model.predict([[i]])}')
