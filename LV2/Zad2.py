import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

data = np.loadtxt(open(Path("LV2/mtcars.csv"), "rb"), usecols=(1, 2, 3, 4, 5, 6), delimiter=",", skiprows=1)

plt.scatter(data[:, 3], data[:, 0])

sizes = 1000 * data[:, 5] / max(data[:, 5])
plt.scatter(data[:, 3], data[:, 0], s=sizes)

mpg_min = min(data[:, 0])
mpg_max = max(data[:, 0])
mpg_mean = np.mean(data[:, 0])
print("Minimalna potrosnja (mpg): ", mpg_min)
print("Maksimalna potrosnja (mpg): ", mpg_max)
print("Srednja potrosnja (mpg): ", mpg_mean)

data_6cyl = data[data[:, 1] == 6]
mpg_6cyl_min = min(data_6cyl[:, 0])
mpg_6cyl_max = max(data_6cyl[:, 0])
mpg_6cyl_mean = np.mean(data_6cyl[:, 0])
print("Minimalna potrosnja (mpg) za 6-cilindricne automobile: ", mpg_6cyl_min)
print("Maksimalna potrosnja (mpg) za 6-cilindricne automobile: ", mpg_6cyl_max)
print("Srednja potrosnja (mpg) za 6-cilindricne automobile: ", mpg_6cyl_mean)

plt.xlabel("Konjska snaga (hp)")
plt.ylabel("Potrosnja (mpg)")
plt.title("Task 2")
plt.show()