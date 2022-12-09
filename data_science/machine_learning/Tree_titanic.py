import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import tree

pd.set_option('display.max_columns', None)
df = pd.read_csv('Tree_titanic.csv')
print(df.describe())

inputs = df.drop(['Survived', 'PassengerId', 'Name', 'Ticket', 'Embarked', 'Cabin', 'Parch', 'SibSp'], axis='columns')
target = df['Survived']

le_sex = LabelEncoder()
inputs['Sex_n'] = le_sex.fit_transform(inputs['Sex'])
inputs = inputs.drop(['Sex'], axis='columns')
inputs = inputs.drop(['Fare'], axis='columns')

mean_age = inputs['Age'].mean()
median_age = inputs['Age'].median()
set_age = 10000
print(mean_age, median_age)
inputs['Age'].fillna(value=set_age, inplace=True)


X_train, X_test, y_train, y_test = train_test_split(inputs, target, test_size=0.8)

model = tree.DecisionTreeClassifier()
model.fit(X_train, y_train)

print(inputs)
print(model.score(X_test, y_test))
print(model.predict([[1, 38, 0]]))



