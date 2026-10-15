def conversion(num):
    if num == 1:
        return "Lunes"

    elif num == 2:
        return "Martes"

    elif num == 3:
        return "Miércoles"

    elif num == 4:
        return "Jueves"

    elif num == 5:
        return "Viernes"

    elif num == 6:
        return "Sábado"

    elif num == 7:
        return "Domingo"

    else:
        return "No existe el día"

def piramide(num):
    for n in range(num,0,-1):
        print()
        for m in range(n, 0, -1):
            print(m, end= " ")
    print()

def comp(num1, num2):
    if num1 == num2:
        return "Son iguales"

    elif num1 > num2:
        return "El primero es mayor que el segundo"

    else:
        return "El segundo es mayor que el primero"

def contar(texto, letra):
    cont = 0
    for i in texto:
        if i == letra:
            cont = cont + 1
    return cont

def diccionario(string):
    diccionario = {}

    for letra in string:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    return diccionario

def elementos(lista,comando,elemento=None):
    
    if comando == "add":
        lista.append(elemento)

    elif comando == "remove":
        lista.remove(elemento)

    else:
        print("Comano erróneo")

    print(lista)

def frase(*palabras):
    string = ""
    for palabra in palabras:
        string = string + palabra + " "

    return string

def fibo(num:int):
    if num <= 1:
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)

def cuadrado(lado):
    area = lado**2
    return area

def triangulo(base, altura):
    area = (base * altura) / 2
    return area

def circulo(radio):
    import math
    area = math.pi * radio**2
    return area