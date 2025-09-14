# grupo 1
# 1. Suma hasta que el usuario ingrese 0
# suma = 0

# while True:
#     num = int(input("Ingrese un número (0 para salir): "))
#     if num == 0:
#         break
#     suma += num

# print("La suma total es:", suma)




# 2. Simulación de pago de deuda con intereses
# deuda = float(input("Ingrese el monto de la deuda: "))
# tasa = float(input("Ingrese la tasa de interés mensual (%): ")) / 100
# meses = int(input("Ingrese el número de meses: "))
# pago = float(input("Ingrese el pago mensual: "))

# for mes in range(1, meses + 1):
#     interes = deuda * tasa
#     deuda = deuda + interes - pago
#     if deuda <= 0:
#         print(f"La deuda se pagó totalmente en el mes {mes}")
#         break
#     print(f"Mes {mes}: Interés = {interes:.2f}, Deuda restante = {deuda:.2f}")





# Grupo 2
# 2. Contador de intentos fallidos de clave
# clave_correcta = "1234"
# intentos = 0

# while True:
#     clave = input("Ingrese la clave: ")
#     if clave == clave_correcta:
#         print("✅ Acceso permitido")
#         break
#     else:
#         intentos += 1
#         print("❌ Clave incorrecta. Intentos fallidos:", intentos)

# 3. Simulación de stock en una mina
# stock = int(input("Ingrese el stock inicial de la mina: "))

# while stock > 0:
#     extraccion = int(input("Ingrese la cantidad a extraer: "))
#     if extraccion > stock:
#         print("No hay suficiente stock. Stock actual:", stock)
#     else:
#         stock -= extraccion
#         print("Stock restante:", stock)

# print("⚠️ El stock se ha agotado")



# Grupo 3
# 3. Calcular clics acumulados hasta 1000
# clics = 0

# while clics < 1000:
#     nuevo_clic = int(input("Ingrese cantidad de clics: "))
#     clics += nuevo_clic
#     print("Clics acumulados:", clics)

# print("✅ Se alcanzaron los 1000 clics")

# 4. Promedio de calificaciones de atención
# total = 0
# cantidad = 0

# while True:
#     calificacion = int(input("Ingrese calificación (1 a 10, 0 para salir): "))
#     if calificacion == 0:
#         break
#     if 1 <= calificacion <= 10:
#         total += calificacion
#         cantidad += 1
#     else:
#         print("⚠️ Calificación no válida")

# if cantidad > 0:
#     promedio = total / cantidad
#     print("El promedio de satisfacción es:", promedio)
# else:
#     print("No se ingresaron calificaciones válidas")




# Nivel básico
# 1. Imprimir números del 1 al 5
i = 1
while i <= 5:
    print(i)
    i += 1

# 2. Números pares desde 3 hasta 15
i = 3
while i <= 15:
    if i % 2 == 0:
        print(i)
    i += 1








# 3. Cuenta regresiva desde 5 hasta 1
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# 4. Imprimir "Python es genial" 3 veces
# i = 0
# while i < 3:
#     print("Python es genial")
#     i += 1

# ✅ Nivel intermedio
# 1. Pedir números hasta que el usuario escriba 0
# num = int(input("Ingrese un número (0 para salir): "))

# while num != 0:
#     print("Ingresaste:", num)
#     num = int(input("Ingrese otro número (0 para salir): "))

# print("Programa terminado")

# clave = ""
# while clave != "python123":
#     clave = input("Ingrese la contraseña: ")

# print("✅ Contraseña correcta")


# 3. Contar números hasta que el usuario ingrese -1
# contador = 0
# num = int(input("Ingrese un número (-1 para terminar): "))

# while num != -1:
#     contador += 1
#     num = int(input("Ingrese un número (-1 para terminar): "))

# print("Cantidad de números ingresados:", contador)

# 4. Adivinar número secreto (7)
# numero_secreto = 7
# num = None

# while num != numero_secreto:
#     num = int(input("Adivina el número secreto: "))

# print("🎉 ¡Adivinaste el número!")

# 5. Nota entre 0 y 20
# nota = -1

# while nota < 0 or nota > 20:
#     nota = int(input("Ingrese una nota (0-20): "))

# print("Nota válida ingresada:", nota)