monto = int(input("Ingrese su monto: "))

if monto >= 1000:
    print("Es mayor a 1000")
else:
    print("Es menor a 1000")
    
    
# Ejercicio 1: Clasificación de riesgo Dado el ingreso mensual y el nivel de deuda,
# imprimir: "Riesgo Bajo" si deuda < 30% del ingreso. "Riesgo Medio" 
# si deuda entre 30% y 50%. "Riesgo Alto" si deuda > 50%.

ingreso = int(input("Registre su ingreso: "))
deuda = int(input("Registre su deuda: "))

if deuda < 0.3 * ingreso:
    print("Riesgo Bajo")
elif deuda < 0.5 * ingreso:
    print("Riesgo Medio")
else:
    print("Riesgo Alto")
 

# Ejercicio 2: Simulación de aprobación Preguntar ingreso, score y deudas.
# Aprobar solo si: ingreso ≥ 5000 score ≥ 700 deuda ≤ 40% ingreso.

ingreso = int(input("Registre su ingreso: "))
score = int(input("Registre su score: "))
deuda = int(input("Registre su deuda: "))

if ingreso >= 5000 and score >= 700 and deuda <= 0.4 * ingreso:
    print("Aprobado")
else:
    print("Rechazado")
 

# Ejercicio 3: Rango de montos de crédito Según ingreso,
# asignar el monto máximo de préstamo: ≥ 10000: hasta 80,000 7000–9999:
# hasta 50,000 < 7000: hasta 20,000


ingreso = int(input("Registre su ingreso: "))

if ingreso >= 10000:
  print("Hasta 80,000")

elif ingreso >= 7000:
  print("Hasta 50,000")

else:
  print("Hasta 20,000")

 
 

# Ejercicio 4: Calcular la cuota mensual de un préstamo usando if para definir
# la tasa según plazo (12, 24 o 36 meses).

plazo = int(input("Registre su plazo: "))

if plazo == 12:
    tasa = 0.1
elif plazo == 24:
    tasa = 0.15
else:
    tasa = 0.2

print("La tasa es: ", tasa)
