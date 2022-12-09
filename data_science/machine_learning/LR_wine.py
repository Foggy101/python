import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv('winequality-red.csv')
variables = [var for var in df.columns]
all_vars = (True, variables[5])


def draw_graphs():
    if all_vars[0]:
        for i in range(len(variables)-1):
            x_index = i
            plt.plot(df[variables[x_index]], df['quality'], 'ro')
            plt.xlabel(variables[x_index])
            plt.ylabel('Wine quality')
            plt.title('Wine quality graph')
            plt.show()
    else:
        plt.plot(df[all_vars[1]], df['quality'], 'bo')
        plt.xlabel(all_vars[1])
        plt.ylabel('Wine quality')
        plt.title('Wine quality graph')
        plt.show()


reg = linear_model.LinearRegression()
reg.fit(df[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide',
            'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']], df[['quality']])

print(f'COEF: {reg.coef_*100}, BIAS: {reg.intercept_}')
draw_graphs()


def predict_all():
    score = 0
    for i in range(0, 1599):
        temp = df.values[i][:-1]
        prediction = reg.predict([temp])
        actual = df.values[i][-1]
        print(f'PREDICTION: {prediction}, ACTUAL: {actual} ', end='')
        if abs(prediction - actual) > 1:
            print('PREDICTION BAD')
        else:
            print('PREDICTION GOOD')
            score += 1
    print(f'SCORE = {score}, accuracy = {score / 1599}')


predict_all()

