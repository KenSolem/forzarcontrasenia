def main():
  print("**INICIO**")

  responde_estimulos = input("¿La víctima responde a estímulos? (s/n): ").lower()

  if responde_estimulos == "s":
    print("Valorar la necesidad de llevar a la víctima a un hospital cercano.")
    print("**FIN**")
    return
  else:
    print("**Abrir las vías aéreas**")

  while True:
    respira = input("¿La víctima respira? (s/n): ").lower()

    if respira == "s":
      print("Permitir a la víctima una posición de suficiente ventilación.")
      print("**FIN**")
      break

    else:
      print("**Administrar 5 ventilaciones y llamar a la ambulancia**")
    signos_vida = input("¿La víctima presenta signos de vida? (s/n): ").lower()

    if signos_vida == "s":
      print("Reevaluar a la víctima a la espera de la llegada de la ambulancia.")
    else:
      print("**Administrar compresiones torácicas**")
    llego_ambulancia = input("¿Llegó la ambulancia? (s/n): ").lower()
    
    if llego_ambulancia == "s":
      print("**FIN**")
      break
main()
