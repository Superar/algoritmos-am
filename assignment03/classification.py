#! /usr/bin/env python3
import urllib.request
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets.base import load_iris
from sklearn.model_selection import cross_validate
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import Perceptron
from sklearn.svm import SVC


def download_glass_file(filename):
    print('Downloading \'{}\'...'.format(filename), file=sys.stderr)
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/glass/'
    response = urllib.request.urlopen(url + filename)
    data = response.read().decode('utf-8')
    print('Download complete!', file=sys.stderr)
    return data


def download_glass_dataset():
    glass_files = ['glass.data', 'glass.names', 'glass.tag']

    for file_ in glass_files:
        filepath = os.path.join(os.getcwd() + '/glass', file_)
        if not os.path.exists(filepath):
            data = download_glass_file(file_)
            with open(filepath, 'w') as w_file:
                w_file.write(data)
        else:
            print('File \'{}\' already exists.'.format(file_), file=sys.stderr)


def read_glass():
    attribute_names = ['Id', 'RI', 'Na', 'Mg',  # From glass.names
                       'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']
    df = pd.read_csv(os.getcwd() + '/glass/glass.data',
                     header=None,
                     names=attribute_names)
    return df


def run_glass_experiments(data):
    glass_X = data.drop(['Id', 'Type'], axis=1)
    glass_y = data.loc[:, 'Type']

    mlp = MLPClassifier(hidden_layer_sizes=(20, ),
                        activation='logistic',
                        solver='sgd',
                        max_iter=1000)
    svm_rbf = SVC(kernel='rbf')
    svm_sigmoid = SVC(kernel='sigmoid')
    svm_linear = SVC(kernel='linear')
    perceptron = Perceptron(max_iter=1000,
                            tol=1e-3)

    methods = {'MLP': mlp,
               'SVM - RBF': svm_rbf,
               'SVM - Sigmoid': svm_sigmoid,
               'SVM - Linear': svm_linear,
               'Perceptron': perceptron}

    results = list()
    for method in methods:
        results_model = cross_validate(methods[method],
                                       glass_X, y=glass_y, cv=5,
                                       scoring=['accuracy'],
                                       return_train_score=True)
        results_model['method'] = method
        results_model['fold'] = np.arange(1, 6)
        results.append(pd.DataFrame(results_model))
    return pd.concat(results)


def read_iris():
    iris = load_iris()
    return pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                        columns=iris['feature_names'] + ['target'])


def run_iris_experiments(data):
    iris_X = data.drop('target', axis=1)
    iris_y = data.loc[:, 'target']

    mlp = MLPClassifier(hidden_layer_sizes=(20, ),
                        activation='logistic',
                        solver='adam',
                        max_iter=2000)
    svm_rbf = SVC(kernel='rbf')
    svm_sigmoid = SVC(kernel='sigmoid')
    svm_linear = SVC(kernel='linear')
    perceptron = Perceptron(max_iter=1000,
                            tol=1e-3)

    methods = {'MLP': mlp,
               'SVM - RBF': svm_rbf,
               'SVM - Sigmoid': svm_sigmoid,
               'SVM - Linear': svm_linear,
               'Perceptron': perceptron}

    results = list()
    for method in methods:
        results_model = cross_validate(methods[method],
                                       iris_X, y=iris_y, cv=5,
                                       scoring=['accuracy'],
                                       return_train_score=True)
        results_model['method'] = method
        results_model['fold'] = np.arange(1, 6)
        results.append(pd.DataFrame(results_model))
    return pd.concat(results)


def plot_results(results):
    results_by_method = results.groupby('method')
    for i, (key, _) in enumerate(results_by_method):
        plot_x_ticks = results_by_method.get_group(key)['fold']
        plot_x = plot_x_ticks + np.arange(5)
        plt.xticks(plot_x, plot_x_ticks)
        plot_x += (i - i // 2) * 0.3 * (-1)**i
        plot_y = results_by_method.get_group(key)['test_accuracy'] * 100
        plt.bar(plot_x, plot_y, width=0.3, label=key)
    plt.legend()
    plt.xlabel('Fold')
    plt.ylabel('Test Accuracy (%)')
    plt.show()


def main():

    # GLASS dataset
    if not os.path.exists(os.getcwd() + '/glass'):
        os.mkdir(os.getcwd() + '/glass')
    download_glass_dataset()

    glass_data = read_glass()
    glass_results = run_glass_experiments(glass_data)
    plot_results(glass_results)

    iris_data = read_iris()
    iris_results = run_iris_experiments(iris_data)
    plot_results(iris_results)


if __name__ == "__main__":
    main()
