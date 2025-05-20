# 1- Cuando el juego arranca la máquina debe elgir un número entre 0 - 9
# 2- Debe perdir al usuario que ingrese un número de tres dígitos, se lo pide por la terminal
# 3 - Si se acierta el número pero no la posición cuenta como un herido
# 4 - Si acierta posición y número cuenta como un muerto
# 4 - si tiene tres muertos gana

import random 

lista_numeros = [0,1,2,3,4,5,6,7,8,9]
seleccion_maquina = random.sample(lista_numeros, 3)

while True: 

    muerto = 0
    herido = 0

    entrada_usuario = input("Ingrese un número de 3 dígitos: ")
    if len(entrada_usuario) != 3:
        print("El número debe ser de tres dígitos!!")
        continue

    seleccion_usuario = []

    for num in entrada_usuario:
        seleccion_usuario.append(int(num))

    for index_maquina, valor_maquina in enumerate(seleccion_maquina):
        for index_usuario, valor_usuario in enumerate(seleccion_usuario):
            if index_maquina == index_usuario and valor_maquina == valor_usuario:
                muerto = muerto + 1
            elif valor_maquina == valor_usuario:
                herido = herido + 1

    if muerto == 3:
        print("Ganaste !!!!")
        break


    print(f"Tienes {muerto} muerto y {herido} heridos")

    # print(seleccion_usuario, "Usuario")
    # print(seleccion_maquina, "Maquina")


