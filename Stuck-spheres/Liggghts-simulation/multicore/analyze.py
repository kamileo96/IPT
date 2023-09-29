import numpy as np, matplotlib.pyplot as plt
x,y = np.genfromtxt("wyniki_final.txt", delimiter=' ', dtype=float, usecols=(0,1), unpack=True)
print(len(x), f" wyników. Wszystkie wypadły {np.sum(x>450)/len(x):.2f} razy")
plt.plot(x,y, '.')
plt.show()
plt.hist(x, np.arange(0, 100, 10))
plt.show() 