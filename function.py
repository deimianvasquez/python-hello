def sum(*args):
    result = ""
    total = 0
    for num in args:
        if type(num) == int or type(num) == float:
            total = total + num
        else:
            result = result + num

    return f"El total a pagar son: {num} $"
    # return f"Es resultado es: {num1 + num2}" ## despues del return


# print("Esto no se ejecuta")
# print(sum(1066, 58, 59, "hola", 10.10))

multi = lambda *args : args

my_list = ["Valentina", "Juan", "Alvaro", "Valentina", "Andreś", "Javiera", "Daniela"]

# def buscar_valentina(item):
#     return item != "Alvaro"

# result = list(filter(buscar_valentina, my_list))
# print(result)


result = list(filter(lambda item:item != "Alvaro" , my_list))
print(result)


result_map = list(map(lambda item : item.upper(), my_list))
print(result_map)




