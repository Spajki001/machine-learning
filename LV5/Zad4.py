# TODO finish this code to do the same as Zad3.py but with color image

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
from sklearn.cluster import KMeans

# Učitaj sliku
img = image.imread("example.png")

# Prikazi sliku
plt.figure()
plt.title('Original image')
plt.imshow(img)

# Pretvori sliku u vektor
h, w, _ = img.shape
img_vector = img.reshape(h * w, -1)

# Primijeni K-means na vektor (sliku)
n_colors = 8  # Broj boja za kvantizaciju
kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(img_vector)

# Zamijeni svaku boju piksela s najbližim centrom
img_compressed = kmeans.cluster_centers_[kmeans.labels_]
img_compressed = img_compressed.reshape(h, w, -1)

# Prikazi kvantiziranu sliku
plt.figure()
plt.title('Quantized image')
plt.imshow(img_compressed.astype(np.uint8), cmap='hsv')

plt.show()
