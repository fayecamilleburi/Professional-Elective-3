import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Create synthetic data
X, y_true = make_blobs(n_samples=500, centers=4, cluster_std=0.70, random_state=0)

# Fit KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Plot results
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=200, c='red', marker='X', label='Centroids')
plt.title("K-Means Clustering")
plt.legend()
plt.show()

from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load Wine dataset
wine = load_wine()
X = wine.data
y = wine.target

# Apply PCA with 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Create a DataFrame for plotting
df = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
df['target'] = y

# Plot
sns.scatterplot(data=df, x='PC1', y='PC2', hue='target', palette='Set2')
plt.title("PCA Projection of Wine Dataset")
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.2f}% variance)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.2f}% variance)")
plt.show()

# From Activity 3
from sklearn.ensemble import IsolationForest

# Generate normal and outlier points
rng = np.random.RandomState(42)
X = 0.3 * rng.randn(100, 2)
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))
X_combined = np.r_[X + 2, X - 2, X_outliers]

# Fit Isolation Forest
clf = IsolationForest(contamination=0.1)
clf.fit(X_combined)
y_pred = clf.predict(X_combined)

# Visualize
plt.scatter(X_combined[:, 0], X_combined[:, 1], c=y_pred, cmap='coolwarm')
plt.title("Outlier Detection with Isolation Forest")
plt.show()
