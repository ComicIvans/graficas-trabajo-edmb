import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

def ojos_gato():
  # Ask for c valued
  c = input('Introduce el valor de la c (mínimo 1): ')

  # Check if it's a number
  try:
    c = float(c)
  except:
    print('¡Número no válido! Saliendo...')
    return
  
  # Check if it's greater than 1
  if c < 1:
    print('¡Número inferior a 1! Saliendo...')
    return

  x = np.linspace(-5, 5, 100)
  y = np.linspace(-5, 5, 100)
  X, Y = np.meshgrid(x, y)
  Z = -np.log(c * np.cosh(Y) + np.sqrt(c**2 - 1) * np.cos(X))

  plt.figure(1)
  plt.contour(X, Y, Z)
  plt.gca().set_title(f'Ojos de gato para c = {c}')
  plt.show()