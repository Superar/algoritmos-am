#!/usr/bin/env python3
import pandas as pd
from matplotlib import pyplot as plt


def corr(data, features):
    # Correlation between values
    corr_mat = data.loc[:, features].corr()
    plt.matshow(corr_mat)
    plt.xticks(range(len(corr_mat.columns)), corr_mat.columns, rotation=90)
    plt.yticks(range(len(corr_mat.columns)), corr_mat.columns)
    plt.show()

def main():
    df = pd.read_csv('data/train.csv')
    features = df.columns

    # Class balance
    class_balance = df.groupby('target')['target'].count()
    plt.figure(figsize=(8, 8))
    plt.pie(class_balance)
    plt.legend(class_balance.index)
    plt.show()

    # Correlation matrix
    corr_features = {f for f in features if not f.endswith('_cat') and not f.endswith('_bin')}
    corr_features.remove('id')
    corr(df, corr_features)

if __name__ == "__main__":
    main()