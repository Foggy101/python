from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score


digits = load_digits()

# REGULAR TRAIN TEST SPLIT
X = pd.DataFrame(digits.data, columns=digits.feature_names)
y = digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


def create_model(model, x_trainer, x_tester, y_trainer, y_tester):
    model.fit(x_trainer, y_trainer)
    print(f'Model: {str(model).split("(", 1)[0]}, Score: {"{:.3f}".format(model.score(x_tester, y_tester))}')
    return model.score(x_tester, y_tester)


create_model(LogisticRegression(max_iter=10000), X_train, X_test, y_train, y_test)
create_model(SVC(), X_train, X_test, y_train, y_test)
create_model(RandomForestClassifier(), X_train, X_test, y_train, y_test)

test_df = [i for i in range(0, 50)]
kf = KFold(n_splits=10)
# for train_index, test_index in kf.split(test_df):
#     print(train_index, test_index)

scores_lr = []
scores_svm = []
scores_rf = []

folds = StratifiedKFold(n_splits=3)

# COULD BE REPLACE BY CROSS_VAL_SCORE
'''for train_index, test_index in folds.split(digits.data, digits.target):
    X_train, X_test, y_train, y_test = digits.data[train_index], digits.data[test_index],\
                                       digits.target[train_index], digits.target[test_index]

    scores_lr.append(create_model(LogisticRegression(max_iter=10000), X_train, X_test, y_train, y_test))
    scores_svm.append(create_model(SVC(), X_train, X_test, y_train, y_test))
    scores_rf.append(create_model(RandomForestClassifier(n_estimators=30), X_train, X_test, y_train, y_test))

for score in [scores_lr, scores_svm, scores_rf]:
    print(score)'''

print(cross_val_score(LogisticRegression(max_iter=10000), X, y, cv=3))
print(cross_val_score(SVC(), X, y, cv=3))
print(cross_val_score(RandomForestClassifier(n_estimators=30), X, y, cv=3))



