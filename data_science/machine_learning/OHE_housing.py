import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

df = pd.read_csv('housing.csv')

# OHE MANUALLY
dummies = pd.get_dummies(df.town)
merged = pd.concat([df, dummies], axis='columns')
final = merged.drop(['town', 'west windsor'], axis='columns')

reg = linear_model.LinearRegression()
X = final.drop(['price'], axis='columns')
y = final.price
reg.fit(X, y)

#print(reg.coef_, reg.intercept_)
print(reg.predict([[2800, 0, 1]]))
print(reg.score(X, y))

# OHE USING SKLEARN.PREPROCESSING

le = LabelEncoder()
df_le = df
df_le.town = le.fit_transform(df_le.town)
print(df_le)

X = df[['area', 'town']].values
y = df.price.values

ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(categories='auto'), [1])], remainder='passthrough')
X = ct.fit_transform(X)
X = X[:, 1:]

model = linear_model.LinearRegression()
model.fit(X, y)

# print(model.coef_, model.intercept_)
print(model.predict([[1, 0, 2800]]))
print(model.score(X, y))



