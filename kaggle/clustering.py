#! /usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans, AgglomerativeClustering
from sklearn.metrics import homogeneity_completeness_v_measure


def run_experiment(model, data):
    X = data.drop('target', axis=1)
    y = data.loc[:, 'target']

    # Training
    y_pred = model.fit_predict(X)
    homo, comp, v_m = homogeneity_completeness_v_measure(y,
                                                         y_pred)
    print('Homogeneity: {:.2f}%'.format(homo * 100))
    print('Completeness: {:.2f}%'.format(comp * 100))
    print('V-Measure: {:.2f}%'.format(v_m * 100))


def main():
    df = pd.read_csv('data/train.csv')
    data = df.drop('id', axis=1)

    # KMeans - 100%
    print(5*'-', 'KMeans - 100%', 5*'-')
    model = MiniBatchKMeans(n_clusters=100)
    run_experiment(model, data)
    print(20*'-')

    # KMeans - 10%
    df = df.groupby('target').apply(pd.DataFrame.sample,
                                    frac=0.1).reset_index(drop=True)
    data = df.drop('id', axis=1)

    print(5*'-', 'KMeans - 10%', 5*'-')
    model = MiniBatchKMeans(n_clusters=100)
    run_experiment(model, data)
    print(20*'-')

    # Agglomerative Clustering - 10%
    print(5*'-', 'Agglomerative Clustering - 10%', 5*'-')
    model = AgglomerativeClustering(n_clusters=2)
    run_experiment(model, data)
    print(30*'-')


if __name__ == "__main__":
    main()
