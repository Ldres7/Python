def main():
    listaN = [5, 10, 8, 7, 5, 10]
    print(minimo(listaN))
    print(maximo(listaN))
    print(promedio(listaN))
#Ejercicio 2
def ListaNumeros():
    lista = []
    numero = 1
    while numero != 0:
        numero = int(input("Ingresar Numero (0 Para finalizar):"))
        if numero != 0:
            lista.append(numero)
    print(lista)

#Ejercicio 3
"Realizar funciones que retorne el m´aximo y el m´ınimo y promedio de los nu´meros procesados. Considerar nu´meros enteros."
def maximo(lista):
    mayor = lista[0]
    for numero in (lista):
        if numero > mayor:
            mayor = numero
    return(mayor)

def minimo(lista):
    menor = lista[0]
    for numero in (lista):
        if numero < menor:
            menor = numero
    return(menor)

def promedio(lista):
    suma = 0
    for numero in (lista):
        cantidad = len(lista)
        suma = suma+numero
        div = suma/cantidad
    return(float(div))

#Ejercicio 5
def mas7(lista):
    cantidad = 0
    for numero in (lista):
        if numero > 6:
            cantidad += 1
    return(cantidad)

def menos4(lista):
    cantidad = 0
    for numero in (lista):
        if numero < 4:
            cantidad += 1
    return (cantidad)

def entre4y7(lista):
    cantidad = 0
    for numero in (lista):
        if numero >= 4 and numero < 7:
            cantidad += 1
    return(cantidad)

#Ejercicio 6
#Listas:
nombres = ["Juan", "José", "Nadia", "Lucia"]
edades = [26, 24, 16, 19]
def MayoresDeEdad(lista):
    for edad in range (len(lista)):
        if edades[edad] > 17:
            print("Mayores de edad:",nombres[edad])
    print("Promedio de edad:",promedioEdades(lista))
            
def promedioEdades(lista):
    suma = 0
    cantidad = 0
    for edad in range(len(lista)):
        if edades[edad] > 17:
            suma = suma + edades[edad]
            cantidad += 1
            promedio = suma/cantidad
    return(promedio)


    