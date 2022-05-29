import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as colors

a = np.array([1,2,3,4,5])


print((np.where(a == 5)[0][0]))

a[1] = 5
print(a)