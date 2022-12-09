from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score

iris = load_iris()

X = iris.data
y = iris.target

scores_lr = cross_val_score(LogisticRegression(max_iter=10000), X, y, cv=5)
scores_svm = cross_val_score(SVC(), X, y, cv=5)
scores_rf = cross_val_score(RandomForestClassifier(), X, y, cv=5)

print(f'lr: {sum(scores_lr)/len(scores_lr)}')
print(f'svm: {sum(scores_svm)/len(scores_svm)}')
print(f'rf: {sum(scores_rf)/len(scores_rf)}')




