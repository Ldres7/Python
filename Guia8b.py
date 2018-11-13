#Guia8b
#Ejercicio 1
def Temperatura():
    mayor = 0
    menor = 9999999
    for dias in range(1, 7+1):
        print("Ingresar temperatura", dias, ":")
        temp = int(input())
        if temp > mayor:
            mayor = temp
        if temp < menor:
            menor = temp
    print("La temperatura mas alta es:", mayor, "y la mas baja es:", menor)
    
#Ejercicio 2    
def Cuantos():
    mayor = 0
    menor = 0
    for numeros in range (1, 10+1):
        print("Ingrese el", numeros, "numero:")
        num = int(input())
        if num > 0:
            mayor += 1
        if num < 0:
            menor += 1

    print("Numeros mayores a cero:", mayor, "Numeros menores a cero:", menor)


#Ejercicio 3
def NumerosEnteros(cantidad):
    rango1 = 0
    rango2 = 0
    rango3 = 0
    rango4 = 0
    print ("Ingresar", cantidad, "numeros:")
    for numero in range(cantidad):
        numero = int(input())
        rangoNumero(numero)
        if rangoNumero(numero) == "Rango 1":
            rango1 +=1
        if rangoNumero(numero) == "Rango 2":
            rango2 +=1
        if rangoNumero(numero) == "Rango 3":
            rango3 += 1
        if rangoNumero(numero) == "Rango 4":
            rango4 += 1
    print("¿Cuántos están entre el 50 y 75, ambos inclusive?:", rango1)
    print("¿Cuántos mayores de 80?:", rango2)
    print("¿Cuántos menores de 30?:", rango3)
    print("¿Cuántos no estaban en ninguno de los rangos anteriores?:", rango4)
        

def rangoNumero(numero):
    if numero >= 50 and numero <= 75:
        rango = "Rango 1"
    elif numero > 80:
        rango = "Rango 2"
    elif numero < 30:
        rango = "Rango 3"
    else:
        rango = "Rango 4"
    return(rango)

#Ejercicio 4
def DivisoresDe(numero):
    for div in range(1, numero+1):
        if esDivisor(numero, div) == True:
            print(div)

            
    
def esDivisor(numero, div):
    if numero % div == 0:
        Verdad = True
    else:
        Verdad = False
    return (Verdad)


#Ejercicio 5       
def MayorMenor():
    mayor = 0
    num = int(input())
    menor = num
    while num > 0:
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num
        num = int(input())
    print("El mayor es:", mayor, "y el menor es:", menor)


#Ejercicio 6
def sumatoria(numero):
    n = 1
    while numero > 0:
        n = n+numero
        numero -=1
    return (n-1)


#Ejercicio 7
def anioBisiesto(anio):
    bisiesto = anio % 4 == 0    
    bisiesto = anio % (100 and 400) == 0   
    return (bisiesto)

#Ejercicio 8
def DiezA():
    letra = 0
    print("Ingresar letra:")
    while letra < 10:
        if input()=="a":
            letra +=1
        else:
            print("No es la letra a")

#Ejercicio 9
def f(grados):
    fahrenheit = grados*2.12
    return(fahrenheit)

def c(grados):
    celsius = grados/2.12
    return (celsius)


def convertirGrados(tipo, grados):
    f(grados)
    c(grados)
    if tipo == f:
        tipo = f(grados)
    if tipo == c:
        tipo = c(grados)
    return(tipo)
    
    
#Ejercicio 10
def main():
    n = 2
    print("Numero - Cuadrado - Cubo")
    for tabla in range(2, 8):
        Ncc(n)
        n +=1    
    return(Ncc(n))
    
def Ncc(numero):
    print(numero, cuadrado(numero), cubo(numero))
    
def cuadrado(numero):
    cuadrado = numero**2
    return(cuadrado)

def cubo(numero):
    cubo = numero**3
    return(cubo)
        
    

        
        