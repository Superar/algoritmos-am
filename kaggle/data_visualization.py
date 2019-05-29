#!/usr/bin/env python3
import re
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def plot_corr(data, features):
    # Correlation between values
    corr_mat = data.loc[:, features].corr()
    plt.matshow(corr_mat)
    plt.xticks(range(len(corr_mat.columns)), corr_mat.columns, rotation=90)
    plt.yticks(range(len(corr_mat.columns)), corr_mat.columns)
    plt.savefig('img/features_correlation.pdf', format='pdf')
    plt.close()

    # Correlation with respect to the target feature
    target_corr = corr_mat.loc[:, 'target'].drop('target')
    target_corr.plot.barh()
    plt.tight_layout()
    plt.savefig('img/features_target_correation.pdf', format='pdf')
    plt.close()


def plot_feature(data, feature):
    plot_values = data.loc[:, feature]
    plt.boxplot(plot_values)
    plt.xticks(ticks=[1], labels=[feature])
    plt.tight_layout()
    plt.savefig('img/boxplot_'+feature+'.pdf', format='pdf')
    plt.close()


def main():
    df = pd.read_csv('data/train.csv')
    features = df.columns

    # Class balance
    class_balance = df.groupby('target')['target'].count()
    plt.pie(class_balance)
    plt.legend(class_balance.index)
    plt.tight_layout()
    plt.savefig('img/class_balance.pdf', format='pdf')
    plt.close()

    # Correlation matrix
    corr_features = {f for f in features if not re.search('(_cat|_bin)$', f)}
    corr_features.remove('id')
    plot_corr(df, corr_features)

    # Important features selected according to the correlations
    important_features = ['ps_car_13', 'ps_reg_02', 'ps_car_12', 'ps_ind_15']
    for feature in important_features:
        plot_feature(df, feature)

    # From the boxplot: ps_reg_02 is ordinal
    plot_values = df.loc[:, 'ps_reg_02']
    plot_values.plot.hist(edgecolor='black')
    plt.tight_layout()
    plt.savefig('img/hist_ps_reg_02.pdf', format='pdf')
    plt.close()


if __name__ == "__main__":
    main()
