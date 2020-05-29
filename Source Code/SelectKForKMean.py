import PCADataProcessor
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

'''
    This part is used to find the most efficient k to do the k-means algorithm.
'''
def SelectKValue():
    # Store the SSE value.
    SSE = []
    # Do plenty times of K-Means algorithm and recored all the SSE values.
    for k in range(5,21):
        # Do the K-Means.
        estimator = KMeans(n_clusters = k, random_state = 9)
        estimator.fit(PCADataProcessor.PCADataProcessor()[0])
        # Get the SSE values.
        SSE.append(estimator.inertia_)
    # Draw the graph of the k and SSE value.
    X = range(5,21)
    plt.xlabel('k')
    plt.ylabel('SSE')
    plt.plot(X,SSE,'o-')
    plt.show()
    # Store the silhouette score.
    Scores = []
    # Do plenty times of K-Means algorithm and recored all the silhouette score.
    for k in range(5,21):
        # Do the K-Means.
        estimator = KMeans(n_clusters = k, random_state = 9)
        estimator.fit(PCADataProcessor.PCADataProcessor()[0])
        # Get the silhouette score.
        Scores.append(silhouette_score(PCADataProcessor.PCADataProcessor()[0], estimator.labels_, metric = 'euclidean'))
    X = range(5,21)
    # Draw the graph of the k and silhouette score.
    plt.xlabel('k')
    plt.ylabel('Sihouette Coefficient')
    plt.plot(X, Scores, 'o-')
    plt.show()

# Test the function.
SelectKValue()