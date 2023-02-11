"""
Combining PyOD Models
"""

from pyod.models.knn import KNN
from pyod.models.combination import aom, moa, average, maximization


# 0 - Initializing 20 base detectors for combination
k_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140,
            150, 160, 170, 180, 190, 200]

# 1 - Number of classifiers being trained
n_clf = len(k_list)

# 2 - Calculating the Scores
train_scores = np.zeros([X_train.shape[0], n_clf])
test_scores = np.zeros([X_test.shape[0], n_clf])

for i in range(n_clf):
    k = k_list[i]

    clf = KNN(n_neighbors=k, method='largest')
    clf.fit(X_train)

    train_scores[:, i] = clf.decision_scores_
    test_scores[:, i] = clf.decision_function(X_test)

# 3 - Standardizating Scores before Combination
from pyod.utils.utility import standardizer
train_scores_norm, test_scores_norm = standardizer(train_scores, test_scores)

# 4 - Combination
"""
/ Average: average scores of all detectors;

/ Maximization: maximum score across all detectors;

/ Average of Maximum (AOM): divide base detectors into subgroups and take the maximum score for each
subgroup. The final score is the average of all subgroup scores;

/ Maximum of Average (MOA): divide base detectors into subgroups and take the average score for each
subgroup. The final score is the maximum of all subgroup scores.
"""
comb_by_average = average(test_scores_norm)
comb_by_maximization = maximization(test_scores_norm)
comb_by_aom = aom(test_scores_norm, 5) # 5 groups
comb_by_moa = moa(test_scores_norm, 5) # 5 groups