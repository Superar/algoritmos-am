#! /usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans, AgglomerativeClustering
from sklearn.model_selection import train_test_split
from sklearn.metrics import homogeneity_completeness_v_measure
from sklearn.metrics import confusion_matrix


def run_experiment(model, data):
    X = data.drop('target', axis=1)
    y = data.loc[:, 'target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Training
    model.fit(X_train)
    homo, comp, v_m = homogeneity_completeness_v_measure(y_train,
                                                         model.labels_)
    print('Training Homogeneity: {:.2f}%'.format(homo * 100))
    print('Training Completeness: {:.2f}%'.format(comp * 100))
    print('Training V-Measure: {:.2f}%'.format(v_m * 100))

    # Test
    results = model.predict(X_test)
    homo, comp, v_m = homogeneity_completeness_v_measure(y_test,
                                                         results)
    print('\nTesting Homogeneity: {:.2f}%'.format(homo * 100))
    print('Testing Completeness: {:.2f}%'.format(comp * 100))
    print('Testing V-Measure: {:.2f}%'.format(v_m * 100))


def main():
    df = pd.read_csv('data/train.csv')
    data = df.drop('id', axis=1)

    # KMeans
    print(5*'-', 'KMeans', 5*'-')
    model = MiniBatchKMeans(n_clusters=100)
    run_experiment(model, data)
    print(20*'-')

    # Agglomerative Clustering
    print(5*'-', 'Agglomerative Clustering', 5*'-')
    model = AgglomerativeClustering(n_clusters=2)
    run_experiment(model, data)
    print(30*'-')


if __name__ == "__main__":
    main()
