import matplotlib.pyplot as plt
x = [1, 2, 3, 3, 1]
y = [1, 2, 2, 1, 1]
plt.plot(x, y, linewidth=1, marker='*', color='red')
plt.axis([0, 4, 0, 4])
plt.xlabel('x os')
plt.ylabel('y os')
plt.title('Example')
plt.show()
