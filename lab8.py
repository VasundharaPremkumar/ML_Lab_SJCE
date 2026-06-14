# 8)Write a program to perform unsupervised K-means clustering techniques on Iris dataset. 
# K-Means Clustering on Iris Dataset

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load Iris Dataset
iris = load_iris()
X = iris.data

# Apply K-Means with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)

# Predict cluster labels
clusters = kmeans.fit_predict(X)

# Visualize clusters
plt.scatter(X[:,0], X[:,1], c=clusters)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering on Iris Dataset")
plt.show()