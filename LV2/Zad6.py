import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger_color.png")
img = img.copy()

h, w, c = img.shape
print(img.shape)
print(img.dtype)
plt.figure()
plt.imshow(img)
plt.title("Original image")

brighter_img = np.clip(img * [2, 2, 2], 0, 1)
plt.figure()
plt.imshow(brighter_img)
plt.title("Brighter image")

rotated_img = np.zeros((w, h, 3))
for y in range(h):
    for x in range(w):
        rotated_y = x
        rotated_x = h - 1 - y
        rotated_img[rotated_y, rotated_x, :] = img[y, x, :]

mirrored_img = np.zeros((w, h, 3))
for y in range(w):
    for x in range(h):
        mirrored_x = h - 1 - x
        mirrored_img[y, mirrored_x, :] = rotated_img[y, x, :]

fig, axs = plt.subplots(1, 2, figsize=(7, 5))
axs[0].imshow(mirrored_img)
axs[0].set_title("Mirrored image")
axs[1].imshow(rotated_img)
axs[1].set_title("Rotated image (90° right)")

scaling_factor = 10
resized_img = np.zeros((h//scaling_factor, w//scaling_factor, 3))
for y in range(h):
    for x in range(w):
        resized_x = x // scaling_factor
        resized_y = y // scaling_factor
        if_statement_x = (x + scaling_factor) % scaling_factor
        if_statement_y = (y + scaling_factor) % scaling_factor
        if if_statement_x == 0 and if_statement_y == 0:
            resized_img[resized_y, resized_x, :] = img[y, x, :]
plt.figure()
plt.imshow(resized_img)
plt.title("Resized image")

one_fourth_img = np.zeros((h, w, 3))
for y in range(h):
    for x in range(w):
        if 240 <= x < 480:
            one_fourth_img[y, x, :] = img[y, x, :]
plt.figure()
plt.imshow(one_fourth_img)
plt.title("Second 1/4 of the photo")

plt.show()
