import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

digits = load_digits()

print(digits.target_names)

df = pd.DataFrame(digits.data, columns=digits.feature_names)
df['target'] = digits.target

print(df[df.target == 4].head())

X = df.drop(['target'], axis='columns')
y = df.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = SVC(kernel='rbf', gamma='scale')
model.fit(X_train, y_train)
print(model.score(X_test, y_test))




