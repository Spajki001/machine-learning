import matplotlib.pyplot as plt
import funkcija_5_1 as fn
from sklearn.cluster import KMeans

data = fn.generate_data(500, 1)

num_clusters = range(2, 21)
objective_values = []

for k in num_clusters:
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(data)
    objective_values.append(kmeans.inertia_)

plt.plot(num_clusters, objective_values, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Objective Function Value')
plt.title('Objective Function vs. Number of Clusters')
plt.show()
