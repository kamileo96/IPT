import numpy as np, matplotlib.pyplot as plt
x,y = np.genfromtxt("wyniki3.txt", delimiter=' ', dtype=float, usecols=(0,1), unpack=True)
plt.plot(x,y, '.')
plt.show()
plt.hist(x, np.linspace(40, 130, 8))
plt.show()