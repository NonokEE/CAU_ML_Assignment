import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as colors

a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])



plt.figure()
im = plt.imshow(a, cmap=cm.jet, norm=colors.LogNorm())
plt.colorbar(im)
plt.show()