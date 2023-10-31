from ojos_gato import ojos_gato

if __name__ == "__main__":
  number = input("Introduce un número: \n0 - Salir \n1 - Ojos de gato \n")

  if number == "0":
      print("Saliendo...")
      exit()
  elif number == "1":
      ojos_gato()
  else:
      print("¡Número no válido! Saliendo...")
      exit()