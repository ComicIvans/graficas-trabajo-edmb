import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


# Set the points for the contour plot
x = np.linspace(-6, 6, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)

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
  Z = -np.log(c * np.cosh(Y) + np.sqrt(c**2 - 1) * np.cos(X))

  plt.figure(1)
  plt.contour(X, Y, Z)
  plt.gca().set_title(f'Ojos de gato para c = {c}')
  plt.show()

def update_ojos_gato(i):
  plt.clf()
  c = np.linspace(1, 2, 100)[i]
  Z = -np.log(c * np.cosh(Y) + np.sqrt(c**2 - 1) * np.cos(X))
  plt.contour(X, Y, Z)
  plt.gca().set_title(f'Ojos de gato para c = {c}')

def ojos_gato_int():
  fig = plt.figure(1)
  ani = animation.FuncAnimation(fig, update_ojos_gato, frames=100)
  plt.show()
