from plots.ojos_gato import ojos_gato, ojos_gato_ani
from plots.fenvpe import fenvpe
from plots.vortice import vortice
from plots.flujo_deformacion import flujo_deformacion
from plots.flujo_deformacion_girado import flujo_deformacion_girado

if __name__ == "__main__":
  number = input("Introduce un número:\n0 - Salir \n1 - Vórtice\n2 - Flujo de deformación\n3 - Flujo de deformación girado\n4 - Flujos estacionarios no viscosos y periódico-espaciales\n5 - Ojos de gato fijo\n6 - Ojos de gato animado\n")

  if number == "0":
    print("Saliendo...")
    exit()
  elif number == "1":
    vortice()
  elif number == "2":
    flujo_deformacion()
  elif number == "3":
    flujo_deformacion_girado()
  elif number == "4":
    fenvpe()
  elif number == "5":
    ojos_gato()
  elif number == "6":
    ojos_gato_ani()
  else:
    print("¡Número no válido! Saliendo...")
    exit()