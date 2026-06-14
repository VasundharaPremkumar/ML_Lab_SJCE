# Import Iris dataset
from sklearn.datasets import load_iris

# Import PCA
from sklearn.decomposition import PCA

# Import LDA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Import plotting library
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()

# Features
X = iris.data

# Class labels
y = iris.target

# ---------------- PCA ----------------

# Reduce data from 4 dimensions to 2 dimensions
pca = PCA(n_components=2)

# Transform data
X_pca = pca.fit_transform(X)

# Plot PCA result
plt.scatter(X_pca[:,0], X_pca[:,1], c=y)
plt.title("PCA")
plt.show()

# ---------------- LDA ----------------

# Reduce dimensions using class information
lda = LinearDiscriminantAnalysis(n_components=2)

# Transform data
X_lda = lda.fit_transform(X, y)

# Plot LDA result
plt.scatter(X_lda[:,0], X_lda[:,1], c=y)
plt.title("LDA")
plt.show()