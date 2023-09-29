import numpy as np, matplotlib.pyplot as plt, subprocess
import os

import numpy as np

def getRandomPrimeInteger(bounds):

    for i in range(bounds.__len__()-1):
        if bounds[i + 1] > bounds[i]:
            x = bounds[i] + np.random.randint(bounds[i+1]-bounds[i])
            if isPrime(x):
                return x

        else:
            if isPrime(bounds[i]):
                return bounds[i]

        if isPrime(bounds[i + 1]):
            return bounds[i + 1]

    newBounds = [0 for i in range(2*bounds.__len__() - 1)]
    newBounds[0] = bounds[0]
    for i in range(1, bounds.__len__()):
        newBounds[2*i-1] = int((bounds[i-1] + bounds[i])/2)
        newBounds[2*i] = bounds[i]

    return getRandomPrimeInteger(newBounds)

def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
    return count == 1


num = 50
seeds = np.empty(num)
#ex: get 50 random prime integers between 100 and 10000:
bounds = [20000, 1000000]
for i in range(num):
    x = getRandomPrimeInteger(bounds)
    seeds[i] = x


dumpstep = 1000
dt = 0.2e-4

def RunSimulation(seed):
    with open('input.liggghts', 'r', encoding='utf-8') as file:
        data = file.readlines()
    
    data[0] = f"variable seeed equal {seed}\n"
    data[1] = f"variable dumpstep2 equal {dumpstep}\n"
    
    with open('input.liggghts', 'w', encoding='utf-8') as file:
        file.writelines(data)

    subprocess.run(["mpirun", "--cpu-set",  "1", "--bind-to", "core", "-n", "2", "lmp380", "-in", "input.liggghts"])



    directory = 'post'
    
    zfromt = np.array([], dtype=int)
    hasfallen = np.array([0], dtype=int)
    for i in np.arange(dumpstep, 267000, dumpstep):
        filename = f"particles_{i}.txt"
        id, z = np.genfromtxt(f'{directory}/{filename}', delimiter=' ', usecols=(0,4), skip_header=9, unpack=True)
        fallennow = (z < .04)*id
        hasfallen = np.unique(np.concatenate((hasfallen,fallennow),0))
        numz = len(hasfallen) - 1
        zfromt = np.append(zfromt, numz)
        zmax = np.amax(zfromt)
    t = ((np.sum((0 < zfromt) & (zfromt < zmax)))+1)*dt*dumpstep
    print(f"Wypadło {zmax} kulek, w czasie {t*1000:.2f} ms +- {dt*1000} ms")
    return zmax, t
    #plt.plot(zfromt, '.')
    #plt.show()

for seed in seeds:
    zmax, t = RunSimulation(seed)
    with open('wyniki.txt', 'a+', encoding='utf-8') as file:
        file.writelines(f'{zmax} {t:.2f} {seed}\n')

#variable seeed equal 86028157
