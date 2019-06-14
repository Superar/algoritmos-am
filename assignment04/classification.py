#! /usr/bin/env python3
import urllib.request
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xgboost as xgb
from sklearn.model_selection import cross_validate
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from mlxtend.classifier import StackingClassifier
from sklearn.ensemble import VotingClassifier

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


def run_glass_experiments_ensemble(data):
    glass_X = data.drop(['Id', 'Type'], axis=1)
    glass_y = data.loc[:, 'Type']

    bagging = BaggingClassifier(base_estimator=DecisionTreeClassifier(),
                                n_estimators=100)
    boosting = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(),
                                  n_estimators=100)
    stacking = StackingClassifier(classifiers=[DecisionTreeClassifier() for _ in range(100)],
                                  meta_classifier=DecisionTreeClassifier())
    random_forest = RandomForestClassifier(n_estimators=100)
    xgboost = xgb.XGBClassifier()
    decision_tree = DecisionTreeClassifier()

    eclf = VotingClassifier(estimators=[('Bagging', bagging), ('Boosting', boosting), ('Stacking', stacking),
                                        ('Random Forest', random_forest), ('XGBoost', xgboost),
                                        ('Decision Tree', decision_tree)], voting='hard')
    methods = {' Bagging': bagging,
               ' Boosting': boosting,
               ' Stacking': stacking,
               ' Random Forest': random_forest,
               ' XGBoost': xgboost,
               ' Decision Tree': decision_tree,
               'Ensemble': eclf}

    results = list()
    for method in methods:
        results_model = cross_validate(methods[method],
                                       glass_X, y=glass_y, cv=10,
                                       scoring=['accuracy'],
                                       return_train_score=True)
        results_model['method'] = method
        results_model['fold'] = np.arange(1, 11)
        results.append(pd.DataFrame(results_model))
    return pd.concat(results)



def plot_results(dataset, results):
    results_by_method = results.groupby('method')
    for i, (key, _) in enumerate(results_by_method):
        plot_x_ticks = results_by_method.get_group(key)['fold']
        plot_x = plot_x_ticks + np.arange(0, 19, 2)
        plt.xticks(plot_x, plot_x_ticks)
        plot_x += (i - i // 2) * 0.3 * (-1)**i
        plot_y = results_by_method.get_group(key)['test_accuracy'] * 100
        plt.bar(plot_x, plot_y, width=0.3, label=key)
    plt.legend(loc='upper center', fancybox=True, ncol=3,
               bbox_to_anchor=(0.5, 1.25))
    plt.xlabel('%s - Fold' % dataset)
    plt.ylabel('Test Accuracy (%)')
    plt.show()


def main():

    # GLASS dataset
    if not os.path.exists(os.getcwd() + '/glass'):
        os.mkdir(os.getcwd() + '/glass')
    download_glass_dataset()

    glass_data = read_glass()
    glass_results = run_glass_experiments_ensemble(glass_data)
    plot_results('Glass', glass_results)


if __name__ == "__main__":
    main()
