my_list = ["Valentina", "Juan", "Alvaro", "Valentina", "Andreś", "Javiera", "Daniela"]

# print(len(my_list))
# print(my_list[len(my_list)-1])
# print(my_list[-1])
my_list[2] = "Guillermo"
# print(my_list[2])

my_list.append("Valentina")
my_list.insert(len(my_list) -1, "UN nombre nuevo")
# result = my_list.pop()

# print("El eliminado es: "+ result )
# print(f"El eliminado es: {result}")
# my_list.remove("Valentina")
# del my_list[0:3]

# print(my_list)

# for num in range(15, -1, -1): ## for variable range(inicio, final, contador)
#     print(num)


# for index in range(len(my_list)):
#     print(f" {index}: {my_list[index]}")

for index, valor  in enumerate(my_list):
    print(index, valor)


count = 0

while True:
    print(
    """
        Tienes que seleccionar una opción:
        1.- sumar
        0.- salir
    """)
    opcion = int(input("Ingresa un número"))
    if opcion == 1:
        print("Funcion que suma: ")
    elif opcion == 0: 
        break  






