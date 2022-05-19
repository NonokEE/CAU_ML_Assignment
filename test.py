import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as colors

a = np.array([[1,2,3,4,5],
              [1,2,3,4,5],
              [1,2,3,4,5],
              [1,2,3,4,5],
              [1,2,3,4,5]])

b = np.array([[1,1,1,1,1],
              [2,2,2,2,2],
              [3,3,3,3,3],
              [4,4,4,4,4],
              [5,5,5,5,5]])

c = np.dstack([a,b])
print(c)