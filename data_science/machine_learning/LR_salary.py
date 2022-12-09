import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from word2number import w2n
import pickle


def scale(x):
    x = x / 10
    return x


df = pd.read_csv('salary.csv')

mean_test_score = df.test_score.mean()
df.test_score = df.test_score.fillna(mean_test_score)
df.experience = df.experience.fillna('zero')
df.experience = df.experience.apply(w2n.word_to_num)

df[['experience', 'test_score', 'interview_score']] = df[['experience', 'test_score', 'interview_score']].apply(scale)

print(df)
''' #MODEL + SAVE
reg = linear_model.LinearRegression()
reg.fit(df[['experience', 'test_score', 'interview_score']], df.salary)
print(reg.coef_, reg.intercept_)

with open('salary_model', 'wb') as f:
    pickle.dump(reg, f)
'''

with open('salary_model', 'rb') as f:
    reg = pickle.load(f)

predict_data = [0.2, 0.9, 0.6]
print(f'Model prediction for input data: {reg.predict([predict_data])}')


def draw_graph():
    for feature in df.columns.drop('salary'):
        plt.plot(df[feature], df['salary'], 'ro')
        plt.xlabel(feature)
        plt.ylabel('salary')
        plt.xlim([0, 1.1])
        plt.show()


draw_graph()
