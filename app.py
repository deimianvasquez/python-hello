# print("hola")

# Variables --> tipo de datos 
# num1 = 10 # entero
# num2 = "15" # string
# num3 = 10.5
# num4 = {
#     "name":"Deimian"
# }
# num5 = ["hola"]
# num_two = "Hola ¿qué tal?" 
# print(num1 + int(num2))

# Tipo de datos --> Number (integer or float)
# age = 18
# age_sum = input("ingresa una edad: ")
# print(age + int(age_sum))


# None
# def num2():
#     return
# print(num2())

# Array (lista)
# names_arr = ["Deimian", "Juana", "María"]
# print(type(names_arr))

# Diccionarios
# human = {
#     "name":"Deimian Two",
#     "pets": ["Cat", "Dogs"]
# }

# print(human["name"])

# # Objetos 
# class Human():
#     def __init__(self, name):
#         self.name = name

#     def result(self):
#         return self.name

# print(Human("Deimian").result())

# Tuplas

# names = ("Deimian", "Cristian")
# names[0] = "Otro"
# print(names)

# names_arr.append("Juanita")
# print(names_arr)


# Set
# frutas = {"Mango", "Pera", "Manzana"}
# otra_fruta = {"Mango", "Cambur", "Mandarina"}
# print(frutas.intersection(otra_fruta))

# string

# saludo = '''HOla ¿qué tal'''
# print(saludo)


# PI = 3.14159
# name = "Deimian"
# age = 19

# # if age >= 18:
#     print("Eres mayor de edad, puedes votar!!")
# else:
#     print("NO puedes ejercer el voto :(")

siento_que_me_atropello_un_tren = True
me_atropello_un_tren = False


# if siento_que_me_atropello_un_tren == True and me_atropello_un_tren == False:
#     print("Tienes gripe")
   
# else:
#     print("No tienes gripe")


# num1 = 10
# num2 = 20
# user = "deimianv"
# password = "123456"

# result = "deimian@gmail"

# print(num1 == num2)
# print(num1 > num2)
# print(num1 < num2)
# print(num1 != num2)

# my_arr = ["Deimian", "Alvaro", "Cristian"]

# if result is None:
#     print("Sin acceso hermanito") ## 10 lineas de código
# else:
#     print("me trae el usuario")


# if "Deimian" in my_arr:
#     print("Si existe")

# else:
#     print("No existe")


# client_vip = True
# sales_min = False

# if client_vip or sales_min:
#     print("Tienes el descuento")

# else:
#     print("Se niega el descuento ")



# age = 20
# id = True

# if age >= 18 and id == True:
#     print("Puedes ejercer el voto")
# else:
#     print("Necesitas los documentos")


# num = 7

# if num > 0:
#     print("Es positivo")
# elif num < 0:
#     print("Es negativo")
# else:
#     print("Es cero")

"""
    impime los números del 0 al 100
    Si el multiplo de 3 imprime Fizz
    Sí es multiplo de 5 imprime Buzz
    Si es multiplo de 3 y 5 imprime FizzBuzz
    Si no lo es imprime el número 
"""

for index in range(101):
    if index % 3 == 0 and index % 5 == 0:
        print("FizzBuzz")
    elif index % 3 == 0:
        print("Fizz")
    elif index % 5 == 0 :
        print("Buzz")
    else:
        print(index)


valor = 14

if valor < 10:
    print("El valor es una unidad")
elif valor < 100:
    print("El valor es una decena")
elif valor < 1000:
    print("El valor es una centena")
elif valor < 10000:
    print("El valor es una unidad de mil")
else:
    print("El valor es un número más allá de los miles")


