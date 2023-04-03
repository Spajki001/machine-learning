import numpy as np
import matplotlib.pyplot as plt

def blackandwhite_img(square_size, square_amount_h, square_amount_w):
    blue_square = np.zeros((square_size, square_size, 3))
    blue_square[:, :, 2] = 255
    red_square = np.ones((square_size, square_size, 3))
    red_square[:, :, 0] = 255
    rows = []
    for i in range(square_amount_h):
        row = []
        for j in range(square_amount_w):
            if (i+j) % 2 == 0:
                row.append(blue_square)
            else:
                row.append(red_square)
        rows.append(np.hstack(row))
    img = np.vstack(rows)

    return img.astype('uint8')

generated_img = blackandwhite_img(60, 5, 4)
plt.imshow(generated_img, cmap='gray', vmin=0, vmax=255)
plt.show()
