from string import ascii_lowercase

def adivinar_contrasenia(contrasenia):
  intentos = 0
  candidato = ""
  for i in range(len(contrasenia)):
    for letra in ascii_lowercase:
      intentos += 1
      candidato += letra
      if candidato == contrasenia:
        return intentos
    candidato = ""
  return -1

def main():
  #indicar la contraseña para advinar
  contrasenia = "gato"
  intentos = adivinar_contrasenia(contrasenia)


  if intentos == -1:
    print("no se ha podido adivinar la contrasenia.")
  else:
    print(f"se ha adivinado la contraseña en {intentos} intentos.")

main()
