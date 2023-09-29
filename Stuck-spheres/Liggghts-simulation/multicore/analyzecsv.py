import numpy as np, matplotlib.pyplot as plt
num, ms = np.genfromtxt("17.csv", delimiter=',', dtype=float, usecols=(0,1), unpack=True)
x = (ms)#.astype(int)
print(len(x), f" wyników. Wszystkie wypadły {np.sum(x>100)/len(x):.2f} razy")
#plt.plot(x,y, '.')
#plt.show()
plt.hist(x, np.arange(0, 100, 1))
plt.show() 