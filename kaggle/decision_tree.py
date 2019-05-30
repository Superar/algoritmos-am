#!/usr/bin/env python3
import pandas as pd
import pydotplus
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.externals.six import StringIO
from IPython.display import Image  


def plot_dt(clf, feature_cols):
    dot_data = StringIO()
    export_graphviz(clf, out_file=dot_data,  
                    filled=True, rounded=True,
                    special_characters=True,feature_names = feature_cols,class_names=['0','1'])
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
    graph.write_png('img/decision_tree.png')
    Image(graph.create_png())

def resampling(df_train):
    # class count
    count_class_0, count_class_1 = df_train.target.value_counts()
    
    # Divide by class
    df_class_0 = df_train[df_train['target'] == 0]
    df_class_1 = df_train[df_train['target'] == 1]
    
    df_class_0_under = df_class_0.sample(count_class_1)
    
    return pd.concat([df_class_0_under, df_class_1])
    

def main():
    train = pd.read_csv('data/train.csv')
    #test = pd.read_csv('data/test.csv')
    
    train = resampling(train)
    
    #target_count = train.target.value_counts()
    #print('Class 0:', target_count[0])
    #print('Class 1:', target_count[1])
    
    labels = train.columns[2:] # Remove id and target
    X = train[labels]
    y = train['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    
    # Create
    classifier = DecisionTreeClassifier()
    
    # Train
    classifier.fit(X_train, y_train)  
    
    # Predict
    y_pred = classifier.predict(X_test)  
    
    # Evaluate
    print('\nReport: ')
    print(classification_report(y_test, y_pred))
    
    print('\nConfusion Matrix: ')
    print(confusion_matrix(y_test, y_pred))
    
    print('\nAccuracy: ')
    print(accuracy_score(y_test, y_pred)*100)
    
    #plot_dt(classifier,labels)
    
    
if __name__ == "__main__":
    main()
