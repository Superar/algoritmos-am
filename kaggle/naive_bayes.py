import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.metrics import classification_report, confusion_matrix, cohen_kappa_score


def show_confusion_matrix(x_test, y_pred):
    cm = confusion_matrix(x_test['target'], y_pred)
    plt.clf()
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Wistia)
    classNames = ['0','1']
    plt.title('Porto Seguro - Test Data')
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    tick_marks = np.arange(len(classNames))
    plt.xticks(tick_marks, classNames, rotation=45)
    plt.yticks(tick_marks, classNames)
    s = [['TN','FP'], ['FN', 'TP']]
    for i in range(2):
        for j in range(2):
            plt.text(j,i, str(s[i][j])+" = "+str(cm[i][j]))
    plt.show()

# Importing dataset
df = pd.read_csv("data/train.csv")

class_0 = df[df['target']==0]
class_1 = df[df['target']==1]

data = class_1.append(class_0[:len(class_1)]).drop('id',axis=1)

# Split dataset in training and test datasets (Holdout 80/20)
x_train, x_test = train_test_split(data,test_size=0.2, random_state=int(time.time()))

# Train Classifier
gnb = GaussianNB()
gnb.fit(x_train.drop('target',axis=1).values,x_train["target"])

# Values Training
print('Training: ', gnb.score(x_test.drop('target',axis=1), x_test['target']))

# Testing holdout 80% - 20%
y_pred = gnb.predict(x_test.drop('target',axis=1))
print("Holdout 80-20: " + classification_report(y_pred, x_test['target']))
print("Kappa: " + str(cohen_kappa_score(y_pred, x_test['target'])))
show_confusion_matrix(x_test,y_pred)

# Testing holdout all dataset
y_pred_all = gnb.predict(data.drop('target',axis=1))
print("All dataset: "+ classification_report(y_pred_all, data['target']))
print("Kappa: " + str(cohen_kappa_score(y_pred_all, data['target'])))
show_confusion_matrix(data,y_pred_all)

# Cross-Validation k=10
scores = cross_val_score(gnb, data.drop('target',axis=1), data['target'] , cv=10)
print('Acurácia Cross-Validation: %0.2f (+/- %0.2f)' % (scores.mean(), scores.std() * 2))
y_pred_cross = cross_val_predict(gnb, data.drop('target',axis=1), data['target'] , cv=10)
show_confusion_matrix(data,y_pred_cross)