import matplotlib.pyplot as plt
import funkcija_5_1 as fn
from sklearn.cluster import KMeans

data = fn.generate_data(500, 1)

kmeans = KMeans(n_clusters=3)
kmeans.fit(data)

plt.figure()
plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, cmap='Set1')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=250, marker='*', c='blue')
plt.show()