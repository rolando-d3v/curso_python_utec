# 1. Define ingreso_anual(mensual) que devuelva mensual*12
# def ingreso_anual():
#     mensual = int(input("Ingrese su salario mensual: "))
#     return mensual * 12
# print(ingreso_anual())




# def ingreso_anual(mensual):
#     return mensual * 12
# print(ingreso_anual(10))  




# # 2. Crea cpc(gasto, clics) que devuelva 0 si clics = 0, caso contrario: gasto / clics
# def cpc(gasto, clics):
#     if clics == 0:
#         return 0
#     else:
#         return gasto / clics

# # Ejemplos de uso:
# print(cpc(1000, 0))          # 0
# print(cpc(1000, 50))         # 20.0



# def suma(*nums):
#     tot = 0
#     for n in nums:
#         tot += n
#     return tot

# print(suma(1, 2, 3, 4, 50))





# def concat_ws(sep, *palabras):
#     return sep.join(palabras)

# print(concat_ws("peru_", "Hola", "Mundo", "Python"))






# Ejercicios de Recursividad
# Aquí están las soluciones en Python para cada uno de los ejercicios de recursividad, siguiendo los principios de identificar el caso base, el paso recursivo y la validación de entradas.

# 1. Contador Regresivo
# Esta función cuenta hacia atrás desde un número dado hasta 0.

# Caso base: Cuando el número es 0, la función termina.

# Paso recursivo: La función se llama a sí misma con el número - 1.

# Python

def cuenta_regresiva(n: int):
    """
    Cuenta regresivamente desde un número dado hasta 0.
    """
    if n < 0:
        return  # Valida entradas negativas
    if n == 0:
        print(0)  # Caso base
        return
    
    print(n)
    cuenta_regresiva(n - 1)  # Paso recursivo

# Ejemplo de uso
print("1. Contador Regresivo:")
cuenta_regresiva(5)
print("-" * 20)



# 2. Suma de los Primeros N Números Naturales
# Esta función calcula la suma de los primeros n números naturales de forma recursiva.

# Caso base: Cuando n es 0, la suma es 0.

# Paso recursivo: Retorna n más la suma de los números hasta n−1.

# Python

def suma_naturales(n: int) -> int:
    """
    Calcula la suma de los primeros n números naturales.
    """
    if n < 0:
        return 0 # Valida entradas negativas
    if n == 0:
        return 0  # Caso base
    else:
        return n + suma_naturales(n - 1)  # Paso recursivo

# Ejemplo de uso
print("2. Suma de Números Naturales:")
print(f"La suma de los primeros 5 números es: {suma_naturales(5)}")
print("-" * 20)



# 3. Precio Mayor en una Lista
# Esta función encuentra el precio mayor en una lista usando recursividad.

# Caso base: Cuando la lista tiene un solo elemento, ese es el mayor.

# Paso recursivo: Compara el primer elemento con el mayor del resto de la lista.

# Python

def precio_mayor(precios: list) -> float:
    """
    Encuentra el precio mayor en una lista de precios.
    """
    if not precios:
        return 0 # Valida listas vacías
    if len(precios) == 1:
        return precios[0]  # Caso base
    else:
        # Paso recursivo: Compara el primer elemento con el mayor del resto de la lista
        return max(precios[0], precio_mayor(precios[1:]))

# Ejemplo de uso
print("3. Precio Mayor en una Lista:")
lista_precios = [25.5, 30.0, 15.75, 50.2]
print(f"El precio mayor en {lista_precios} es: {precio_mayor(lista_precios)}")
print("-" * 20)


# 4. Suma de Ventas en un Diccionario Anidado
# Esta función suma todas las ventas en un diccionario de ventas por categoría, que puede contener diccionarios anidados.

# Caso base: Si el valor no es un diccionario, se suma a la cuenta total.

# Paso recursivo: Si el valor es un diccionario, se llama a la función recursivamente para sumar sus valores.

# Python

def sumar_ventas(ventas: dict) -> float:
    """
    Suma todas las ventas en un diccionario, incluyendo diccionarios anidados.
    """
    total = 0
    for valor in ventas.values():
        if isinstance(valor, dict):
            total += sumar_ventas(valor)  # Paso recursivo
        else:
            total += valor  # Caso base
    return total

# Ejemplo de uso
print("4. Suma de Ventas:")
diccionario_ventas = {
    "electronica": 1500,
    "libros": 500,
    "ropa": {
        "verano": 800,
        "invierno": 1200
    }
}
print(f"El total de ventas es: {sumar_ventas(diccionario_ventas)}")
print("-" * 20)



# 5. Deudas que Superan un Umbral
# Esta función cuenta cuántas deudas superan un umbral dado en una lista.

# Caso base: Si la lista está vacía, el conteo es 0.

# Paso recursivo: Si la primera deuda supera el umbral, se cuenta como 1 y se suma al conteo del resto de la lista. Si no, solo se suma el conteo del resto de la lista.

# Python

def deudas_sobre_umbral(deudas: list, umbral: float) -> int:
    """
    Cuenta las deudas que superan un umbral.
    """
    if not deudas:
        return 0  # Caso base: Lista vacía
    
    primer_deuda = deudas[0]
    resto_deudas = deudas[1:]
    
    # Paso recursivo
    if primer_deuda > umbral:
        return 1 + deudas_sobre_umbral(resto_deudas, umbral)
    else:
        return deudas_sobre_umbral(resto_deudas, umbral)

# Ejemplo de uso
print("5. Deudas que Superan un Umbral:")
lista_deudas = [500, 1200, 800, 1500, 200]
print(f"Número de deudas mayores a 1000: {deudas_sobre_umbral(lista_deudas, 1000)}")
print("-" * 20)



# 6. Productos con Descuento
# Esta función cuenta el número de True en una lista de booleanos.

# Caso base: Si la lista está vacía, el conteo es 0.

# Paso recursivo: Si el primer elemento es True, se suma 1 al conteo del resto de la lista. Si es False, se suma 0.

# Python

def contar_descuentos(descuentos: list) -> int:
    """
    Cuenta cuántos productos tienen descuento (True en la lista).
    """
    if not descuentos:
        return 0  # Caso base: Lista vacía
    
    # Paso recursivo
    if descuentos[0]:
        return 1 + contar_descuentos(descuentos[1:])
    else:
        return contar_descuentos(descuentos[1:])

# Ejemplo de uso
print("6. Productos con Descuento:")
lista_descuentos = [True, False, True, True, False]
print(f"Número de productos con descuento: {contar_descuentos(lista_descuentos)}")
print("-" * 20)



# 7. Contar una Palabra Clave
# Esta función cuenta cuántas veces aparece una palabra clave en una lista de cadenas.

# Caso base: Si la lista está vacía, el conteo es 0.

# Paso recursivo: Si la primera campaña contiene la palabra clave, se suma 1. Luego se llama a la función para el resto de la lista.

# Python

def contar_palabra_clave(campanas: list, palabra: str) -> int:
    """
    Cuenta cuántas veces aparece una palabra clave en una lista de campañas.
    """
    if not campanas:
        return 0  # Caso base: Lista vacía
    
    # Normalizamos el texto para una comparación insensible a mayúsculas/minúsculas
    primera_campana_limpia = campanas[0].lower()
    
    # Paso recursivo
    if palabra.lower() in primera_campana_limpia:
        return 1 + contar_palabra_clave(campanas[1:], palabra)
    else:
        return contar_palabra_clave(campanas[1:], palabra)

# Ejemplo de uso
print("7. Contar Palabra Clave:")
lista_campanas = ["Venta de Verano", "Promoción de Invierno", "Venta Especial"]
palabra_buscar = "venta"
print(f"La palabra '{palabra_buscar}' aparece {contar_palabra_clave(lista_campanas, palabra_buscar)} veces.")
print("-" * 20)



