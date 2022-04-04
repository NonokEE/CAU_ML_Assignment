import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as colors

I = np.array([[1, 2, 3],
              [10, 20, 30],
              [100, 200, 300]])

forward_shifted = np.concatenate([I[1:, :], I[-1:, :]])
D = np.subtract(forward_shifted, I)

backward_shifted = np.concatenate([I[:1, :], I[:-1, :]])
B = np.subtract(I, backward_shifted)

print(forward_shifted)
print(D)

print("---------------------")

print(backward_shifted)
print(B)