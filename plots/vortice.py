import matplotlib.pyplot as plt
import numpy as np


# Set the points for the contour plot
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)

def vortice():
  Z = X*X + Y*Y

  plt.figure(1)
  plt.contour(X, Y, Z)
  plt.gca().set_title(f'Vórtice')
  plt.show()