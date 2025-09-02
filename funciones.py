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





def concat_ws(sep, *palabras):
    return sep.join(palabras)

print(concat_ws("peru_", "Hola", "Mundo", "Python"))
