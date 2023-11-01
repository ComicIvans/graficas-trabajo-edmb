import matplotlib.pyplot as plt
import numpy as np


# Set the points for the contour plot
x = np.linspace(-1, 1, 200)
y = np.linspace(-1, 1, 200)
X, Y = np.meshgrid(x, y)

def fenvpe():
  Z = (1/(2.*np.pi))*np.sin(2.*np.pi*X)*np.cos(2.*np.pi*Y)

  plt.figure(1)
  plt.contour(X, Y, Z)
  plt.gca().set_title(f'Flujos estacionarios no viscosos y periódico-espaciales')
  plt.show()