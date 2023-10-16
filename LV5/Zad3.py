import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image 
from sklearn.cluster import KMeans

# ucitaj sliku
img = image.imread("example_grayscale.png")

# prikazi sliku
plt.figure()
plt.title('Original image')
plt.imshow(img, cmap='gray')

# predstavi sliku kao vektor
h, w = img.shape
img_vector = img.reshape(h * w, 1)

# primijeni K-means na vektor (sliku)
n_colors = 3
kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(img_vector)

# zamijeni svjetlinu svakog piksela s najblizim centrom
img_compressed = kmeans.predict(img_vector)
img_compressed = img_compressed.astype(np.float32)

for i in range(0, n_colors):
    img_compressed[img_compressed==i] = kmeans.cluster_centers_[i]

img_compressed = img_compressed.reshape(h, w)

# prikazi dobivenu aproksimaciju (sliku)
plt.figure()
plt.title('Compressed image')
plt.imshow(img_compressed, cmap='gray')
plt.show()
