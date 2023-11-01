import matplotlib.pyplot as plt
import numpy as np


# Set the points for the contour plot
x = np.linspace(-1, 1, 200)
y = np.linspace(-1, 1, 200)
X, Y = np.meshgrid(x, y)

def flujo_deformacion_girado():
  Z = X*X - Y*Y

  plt.figure(1)
  plt.contour(X, Y, Z)
  plt.gca().set_title(f'Flujo de deformación girado')
  plt.show()