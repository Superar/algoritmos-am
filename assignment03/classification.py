#! /usr/bin/env python3
import urllib.request
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
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
        filepath = os.path.join('assignment03/glass', file_)
        if not os.path.exists(filepath):
            data = download_glass_file(file_)
            with open(filepath, 'w') as w_file:
                w_file.write(data)
        else:
            print('File \'{}\' already exists.'.format(file_), file=sys.stderr)


def read_glass():
    attribute_names = ['Id', 'RI', 'Na', 'Mg',  # From glass.names
                       'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']
    df = pd.read_csv('assignment03/glass/glass.data',
                     header=None,
                     names=attribute_names)
    return df


def run_glass_experiments(data):
    glass_X = data.drop(['Id', 'Type'], axis=1)
    glass_y = data.loc[:, 'Type']
    mlp = MLPClassifier(hidden_layer_sizes=(20, ),
                        activation='logistic',
                        solver='sgd',
                        max_iter=500)
    results_mlp = cross_validate(mlp, glass_X, y=glass_y, cv=5,
                                 scoring=['accuracy'],
                                 return_train_score=True)
    results_mlp = pd.DataFrame.from_dict(results_mlp)
    return results_mlp


def main():

    # GLASS dataset
    if not os.path.exists('assignment03/glass'):
        os.mkdir('assignment03/glass')
    download_glass_dataset()

    glass_data = read_glass()
    glass_results = run_glass_experiments(glass_data)
    plt.bar(glass_results.index,
            glass_results.loc[:, 'test_accuracy'])
    plt.show()


if __name__ == "__main__":
    main()
