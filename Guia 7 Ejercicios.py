def Ejercicio1():#esto es un comentario para probar el git
    print("Ingresar numero:")
    numero = int(input())
    print(numero*2)
    
def Ejercicio2():#otro comentario
    print("Ingresar edad:")
    edad = int(input())
    print(edad+23)

def Ejercicio3():
    print("Ingresar precio")
    precio = int(input())
    print("Precio final:", precio*0.91)
    
def Ejercicio4():
    print("Introducir numero")
    numero = int(input())
    
    if numero > 0:
        print("Este numero es positivo")
    else:
        print("Este numero es negativo")

def Ejercicio5():
    print("Ingrese un numero")
    numero = int(input())
    par = numero % 2 == 0
    
    if par:
        print("Es par")
    else:
        print("No es par")

def Ejercicio6():
    print("Ingrese un numero entero")
    numero = int(input())
    multiplo2 = numero % 2 == 0

    if multiplo2:
        print("Es multiplo de 2")
    else:
        print("No es multiplo de 2")
        
def Ejercicio7():
    print("Ingresar dos precios (Decimales)")
    precio1 = float(input())
    precio2 = float(input())
    
    if precio1 < precio2:
        print(precio1,precio2)
    else:
        print(precio2,precio1)
        
def Ejercicio8():
    print("Tiempo de llegada de los 2 autos")
    auto1 = float(input("Auto 1 "))
    auto2 = float(input("Auto 2 "))
    
    if auto1 < auto2:
        print("Primero: Auto 1:","Segundo: Auto 2")
    else:
        print("Primero: Auto 2","Segundo: Auto 1")
       
def Ejercicio9():
    print("Ingresar 3 numeros (Pueden ser enteros)")
    numero1 = int(input("Numero 1 "))
    numero2 = int(input("Numero 2 "))
    numero3 = int(input("Numero 3 "))
    
    if numero1 < 0:
        print(numero1*numero2*numero3)
    else:
        print(numero1+numero2+numero3)

    
def Ejercicio10():
    mayor = 0
    posicion = 0
    for x in range(0, 9):
        num = int(input('Insertar valor: '))
        if num > mayor:
            mayor = num
            posicion = x+1
    print("El número mayor es", mayor, "y se encuentra en la posicion número", posicion)
    
   
    
