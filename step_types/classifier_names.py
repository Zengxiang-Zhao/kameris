from __future__ import absolute_import, division, unicode_literals

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.svm import SVC

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import (
    LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis)

from sklearn.neural_network import MLPClassifier


classifiers_by_name = {
    '10-nearest-neighbors': lambda: KNeighborsClassifier(n_neighbors=10),
    'nearest-centroid-mean': lambda: NearestCentroid(metric='euclidean'),
    'nearest-centroid-median': lambda: NearestCentroid(metric='manhattan'),
    'logistic-regression': lambda: LogisticRegression(),
    'sgd': lambda: SGDClassifier(),
    'linear-svm': lambda: SVC(kernel='linear'),
    'quadratic-svm': lambda: SVC(kernel='poly', degree=2),
    'cubic-svm': lambda: SVC(kernel='poly', degree=3),
    'rbf-svm': lambda: SVC(kernel='rbf'),
    'decision-tree': lambda: DecisionTreeClassifier(),
    'random-forest': lambda: RandomForestClassifier(),
    'adaboost': lambda: AdaBoostClassifier(),
    'gaussian-naive-bayes': lambda: GaussianNB(),
    'lda': lambda: LinearDiscriminantAnalysis(),
    'qda': lambda: QuadraticDiscriminantAnalysis(),
    'multilayer-perceptron': lambda: MLPClassifier()

    # omitted classifiers:
    # 'gaussian-process': lambda: GaussianProcessClassifier(),
    #   *really* slow (and docs say O(n^3))
    # 'multinomial-naive-bayes': lambda: MultinomialNB(),
    #   always gives strange errors
}
