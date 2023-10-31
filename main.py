from plots.ojos_gato import ojos_gato, update_ojos_gato_int

if __name__ == "__main__":
  number = input("Introduce un número:\n0 - Salir \n1 - Ojos de gato fijo\n2 - Ojos de gato interactivo\n")

  if number == "0":
      print("Saliendo...")
      exit()
  elif number == "1":
      ojos_gato()
  elif number == "2":
      update_ojos_gato_int()
  else:
      print("¡Número no válido! Saliendo...")
      exit()