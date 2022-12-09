import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
from matplotlib import style
import pickle

data = pd.read_csv('student-mat.csv', sep=';')

data = data[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences', 'age']]

predict = 'G3'

x = np.array(data.drop(columns=predict))
y = np.array(data[predict])
best = 0
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

''' MODEL SAVE
for i in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)#, random_state=0)

    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print(acc)

    if acc > best:
        best = acc
        with open('studentmodel.pickle', 'wb') as file:
            pickle.dump(linear, file)
'''

pickle_in = open('studentmodel.pickle', 'rb')
linear = pickle.load(pickle_in)

print('Coefficients: ', linear.coef_)
print('Intercept: ', linear.intercept_)

predictions = linear.predict(x_test)

for i in range(len(predictions)):
    print(f'Model prediction: {predictions[i]}, X values: {x_test[i]}, Target value: {y_test[i]}')

style.use('ggplot')
p = 'studytime'
pyplot.scatter(data[p], data['G3'])
pyplot.xlabel(p)
pyplot.ylabel('Final grade')
pyplot.show()

