ventas = {
  "Enero": 15000,
  "Febrero": 22000,
  "Marzo": 12000,
  "Abril": 17000,
  "Mayo": 81000,
  "Junio": 13000,
  "Julio": 21000,
  "Agosto": 41200,
  "Septiembre": 25000,
  "Octubre": 21500,
  "Noviembre": 91000,
  "Diciembre": 21000,
}

def filtrar_ventas(ventas, umbral):

  ventas_filtradas = {}
  for mes, valor in ventas.items():
    if valor > umbral:
      ventas_filtradas[mes] = valor
  return ventas_filtradas

umbral = int(input("Ingrese el umbral de ventas: "))

ventas_mayores = filtrar_ventas(ventas, umbral)

print("Ventas mayores a", umbral, ":")
for mes, valor in ventas_mayores.items():
  print(f"{mes}: {valor}")
