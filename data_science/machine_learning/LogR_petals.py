import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sn


iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)

model = LogisticRegression()
model.fit(X_train, y_train)

print(f'Model score: {model.score(X_test, y_test)}')

i = 120
print(f'Prediction for i = {i}: {model.predict([iris.data[i]])}, Real target: {iris.target[i]}')


y_predicted = model.predict(X_test)
cm = confusion_matrix(y_test, y_predicted)

#plt.figure(figsize=(10, 7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()



