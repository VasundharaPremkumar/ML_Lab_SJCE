# KNN Classifier using Euclidean and Manhattan Distance
# K = 3, Train-Test Split = 70:30

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load dataset using the url given in lab 
df = pd.read_csv("http://10.24.30.48/datasets/glass.csv")
# https://raw.githubusercontent.com/jbrownlee/Datasets/master/glass.csv check this for example where we use url for dataset
# Features and Target
X = df.iloc[:, 1:-1]   # Skip ID column, take feature columns
y = df.iloc[:, -1]     # Last column is target class

# Split data into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Euclidean Distance
knn1 = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
knn1.fit(X_train, y_train)

print("Euclidean Accuracy:",
      knn1.score(X_test, y_test))

# Manhattan Distance
knn2 = KNeighborsClassifier(n_neighbors=3, metric='manhattan')
knn2.fit(X_train, y_train)

print("Manhattan Accuracy:",
      knn2.score(X_test, y_test))