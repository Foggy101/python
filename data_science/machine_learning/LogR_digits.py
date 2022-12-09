import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sn

digits = load_digits()
print(dir(digits))

#print(digits.data)

plt.gray()
plt.matshow(digits.images[15])
plt.show()

X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3)

model = LogisticRegression(class_weight='balanced', max_iter=10000)
model.fit(X_train, y_train)

print(f'SCORE: {model.score(X_test, y_test)}')

i = 15
print(f'PREDICTION FOR i = {i}: {model.predict([digits.data[i]]), digits.target[i]}')

#for i in range(10, 15):
#    print(model.predict([digits.data[i]]))

y_predicted = model.predict(X_test)

cm = confusion_matrix(y_test, y_predicted)
print(cm)

plt.figure(figsize=(10, 7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

