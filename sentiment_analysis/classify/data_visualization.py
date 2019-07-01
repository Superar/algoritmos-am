#!/usr/bin/env python3
from matplotlib import pyplot as plt
from nltk.tokenize import word_tokenize
from classify import load_data
from features import FeatureExtractor
import pandas as pd
import numpy as np


def visualize_class_balance(data_path, classes):
    class_counts = {c: 0 for c in classes}

    for c in classes:
        filename = data_path + '.' + c
        with open(filename) as file_:
            for i, _ in enumerate(file_):
                pass
            class_counts[c] = i+1

    total = sum(class_counts.values()) * 1.0
    class_freqs = [(class_counts[c]/total)*100 for c in classes]
    freqs_str = ['{:.2f}%'.format(f) for f in class_freqs]
    plt.pie(class_freqs, labels=freqs_str)
    plt.legend(classes)
    plt.show()


def visualize_tags(data_path, classes):
    sents, labels, ids = load_data(data_path)

    feats = FeatureExtractor(bow=False, negation=False,
                             emoji=False, senti_words=False,
                             emoticon=False, postag=True,
                             verbose=False)
    feats.make_bow(sents)
    tags = feats.get_representation(sents)

    df = pd.DataFrame(tags, index=ids,
                      columns=['N', 'ADV', 'ADJ', 'V'])
    df['label'] = [classes[l] for l in labels]

    counts = df.groupby('label').sum()
    counts = counts.div(counts.sum(axis=1), axis=0)
    counts *= 100
    counts.plot.bar(rot=0)
    plt.xlabel('Class')
    plt.ylabel('Frequency of PoS tag (%)')
    plt.show()


def visualize_polarities(data_path, classes, lexicon_path):
    lexicon = pd.read_csv(lexicon_path, names=['word', 'sentiment'])
    negative_words = lexicon.loc[lexicon['sentiment'] == -1, 'word']
    neutral_words = lexicon.loc[lexicon['sentiment'] == 0, 'word']
    positive_words = lexicon.loc[lexicon['sentiment'] == 1, 'word']

    sents, labels, ids = load_data(data_path)

    polarity_counts = pd.DataFrame(0, index=['negative', 'neutral', 'positive', 'total'],
                                   columns=classes)

    for i, sent in enumerate(sents):
        class_ = classes[labels[i]]

        tokens = word_tokenize(sent, language='portuguese')
        negative_count = len(set(tokens).intersection(set(negative_words)))
        neutral_count = len(set(tokens).intersection(set(neutral_words)))
        positive_count = len(set(tokens).intersection(set(positive_words)))

        polarity_counts.loc['negative', class_] += negative_count
        polarity_counts.loc['neutral', class_] += neutral_count
        polarity_counts.loc['positive', class_] += positive_count
        polarity_counts.loc['total', class_] += len(tokens)

    polarity_rates = polarity_counts.div(polarity_counts.loc['total', :])
    polarity_rates *= 100

    polarity_rates.loc[polarity_rates.index != 'total', :].T.plot.bar(rot=0)
    plt.xlabel('Class')
    plt.ylabel('Rate of polarity words (%)')
    plt.show()


def main():
    data_path = 'data/corpus/trainTT'
    lexicon_path = 'data/resources/sentilex-reduzido.txt'
    classes = ['neg', 'neu', 'pos']

    visualize_class_balance(data_path, classes)
    visualize_tags(data_path, classes)
    visualize_polarities(data_path, classes, lexicon_path)


if __name__ == "__main__":
    main()
