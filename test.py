import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as colors

I = np.array([[1, 2, 3],
              [10, 20, 30],
              [100, 200, 300]])


a = np.zeros([3,5])

for i in range(3):
    for j in range(5):
        a[i][j] = i+1

print(a)