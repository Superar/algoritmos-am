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
    plt.colorbar()
    plt.savefig('img/features_correlation.pdf',
                format='pdf', bbox_inches='tight')
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
    plt.xticks([1], [feature])
    plt.tight_layout()
    plt.savefig('img/boxplot_'+feature+'.pdf', format='pdf')
    plt.close()


def main():
    df = pd.read_csv('data/train.csv')
    features = df.columns

    # Class balance
    class_balance = df.groupby('target')['target'].count()
    plt.figure(figsize=(6, 6))
    plt.pie(class_balance)
    plt.legend(class_balance.index)
    plt.tight_layout()
    plt.savefig('img/class_balance.pdf', format='pdf')
    plt.close()

    # Separate numerical (ratio and ordinal) and categorical/binary features
    num_features = {f for f in features if not re.search('(_cat|_bin)$', f)}
    cat_bin_features = set(features) - num_features
    num_features.remove('id')
    # Fixate order to prevent inconsistency
    num_features = list(num_features)
    cat_bin_features = list(cat_bin_features)

    # Get basic statistics
    df.loc[:, num_features].describe().to_csv('num_features_statistics.csv')
    cat_bin_df = pd.DataFrame(data=0, index=cat_bin_features,
                              columns=['Mode', 'Count', 'Frequency'])
    cat_bin_df.loc[cat_bin_features, 'Mode'] = df.loc[:,
                                                      cat_bin_features].mode().values
    for feature in cat_bin_features:
        value_counts = df.loc[:, feature].value_counts()
        mode_count = value_counts[cat_bin_df.loc[feature, 'Mode']]
        cat_bin_df.loc[feature, 'Count'] = mode_count

        value_frequency = df.loc[:, feature].value_counts(normalize=True)
        mode_frequency = value_frequency[cat_bin_df.loc[feature, 'Mode']]
        cat_bin_df.loc[feature, 'Frequency'] = mode_frequency*100
    cat_bin_df.to_csv('cat_bin_statistics.csv')

    # Correlation plot
    plot_corr(df, num_features)

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
