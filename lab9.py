from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

# Load Iris Dataset
iris = load_iris()
X = iris.data

# Single Linkage
single = AgglomerativeClustering(
    n_clusters=3,
    linkage='single'
)

single_labels = single.fit_predict(X)

plt.scatter(X[:,0], X[:,1], c=single_labels)
plt.title("Single Linkage")
plt.show()

# Complete Linkage
complete = AgglomerativeClustering(
    n_clusters=3,
    linkage='complete'
)

complete_labels = complete.fit_predict(X)

plt.scatter(X[:,0], X[:,1], c=complete_labels)
plt.title("Complete Linkage")
plt.show()