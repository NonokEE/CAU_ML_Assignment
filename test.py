import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as colors

a = np.array([0,1,0,1,0])
b = np.array([0,1,0,0,1])
res = np.sum(np.abs(a-b))
print(res)

