import numpy as np
import pandas as pd
from sklearn import linear_model


def gradient_descent(x, y):
    m_curr = 0
    b_curr = 0
    learning_rate = 0.00001
    iterations = 1000
    n = len(x)

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y - y_predicted)])
        m_deriv = -(2/n) * sum(x * (y - y_predicted))
        b_deriv = -(2/n) * sum(y - y_predicted)
        m_curr = m_curr - m_deriv * learning_rate
        b_curr = b_curr - b_deriv * learning_rate
        print(f'm: {m_curr}, b: {b_curr}, cost: {cost}, iter: {i}')


df = pd.read_csv('math.csv')
x = np.array(df.math)
y = np.array(df.cs)
z = np.array(df.math)
print(z)


reg = linear_model.LinearRegression()
reg.fit(df[['math']], df[['cs']])


gradient_descent(x, y)
print(reg.coef_, reg.intercept_)
