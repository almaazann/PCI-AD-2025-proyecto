#Aqui se realizara el proyecto de Pensamiento computacional 

"""Algoritmo - Calculadora de ecuaciones cuadráticas, ecuaciones normales y promedio de calificaciones 

ENTRADAS:
-Pedir al usuario determinar si es una ecuacion de primer o segundo grado o si prefiere promediar sus calificaciones
-En caso de ser de primer grado, pedir al usuario como está escrita la ecuacion
-En caso de ser de segundo grado, pedir al usuario que forma tiene la ecuacion y pedir
los coeficientes
-En caso de ser promedio, pedir al usario cuantas calificaciones quiere promediar e invocar la función promedio

PROCESOS
0.-Definir las funcinoes para cada caso (reciclar variable) e importar librerias
1.-PEDIR si es ecuacion de primer o segundo grado
2.-SI es de primer grado:
    2.1.-PEDIR al usuario la forma en la que está escrita la ecuació
    2.2.-Llevar a cabo el calculo del despeje de X
    2.3.-MOSTRAR el valor de X
3.-SINO:
    3.1.-PEDIR al usuario la forma que tiene la ecuación
    3.2.-PEDIR al usuario los coeficientes
    3.3.-Llevar a cabo el calculo para el despeje de X
    3.4.-MOSTRAR el valor de las raíces
4.-SINO: 
    4.1.-PEDIR al usuario la cantidad de calificaciones que quiere promediar (si son 2, 3 o 4 materias)
    4.2.-PEDIR al usuario cada calificacion
    4.3.-INVOCAR la función promedio y hacer el calculo
    4.4.-MOSTRAR el promedio


SALIDAS
Valor de X o de las raíces/0's/X1 y x2"""

import math
import sympy as sp
from sympy import Eq, solve, symbols

#Aquí defino los procesos para ecuaciones cuadraticas, hay 3 tipos:
#mixta(un coeficiente principal y un termino independiente)
#pura(un coeficiente principal y un coeficiente de un termino lineal)
#y la completa (Ax2 + Bx + C = =)

#Ecuacion cuadratica de forma Ax2 + C = 0
def ecuacion2Pura ():    
    coefCuad = int(input('Digite el coeficiente del termino cuadrático: '))
    coefIn = int(input('Digite el coeficiente de el termino independiente: '))
    discriminante = (0-(4*coefCuad*coefIn))
    if discriminante > 0:
       r1 = (0 + math.sqrt(discriminante))/(2*coefCuad)
       r2 = (0 - math.sqrt(discriminante))/(2*coefCuad)
       print(f'Las raíces son {r1:.2f} y {r2:.2f}')
       return None
    else:
        print('El resultado de las raíces son números imaginarios')
        return None
    
#Ecuacion cuadratica de forma Ax2 + Bx = 0
def ecuacion2Mixta():
    coefCuad = int(input('Digite el coeficiente del termino cuadrático: '))
    coefLin = int(input('Digite el coeficiente del termino lineal: '))
    r1 = (-(coefLin) + coefLin)/(2*coefCuad)
    r2 = (-(coefLin) - coefLin)/(2*coefCuad)
    print(f'Las raices son {r1:.2f} y {r2:.2f}')
    return None

#Ecuacion cuadratica de forma completa Ax2 + Bx + C = 0
def ecuacion2Completa():
    coefCuad = int(input('Digite el coeficiente cuadratico: '))
    coefLin = int(input('Digite el coeficiente del termino lineal: '))
    coefIn = int(input('Digite el coeficiente de el termino independiente: '))
    discriminante = (coefLin**2) - (4*coefCuad * coefIn)
    if discriminante > 0:
        r1 = (-coefLin + math.sqrt(discriminante))/(2*coefCuad)
        r2 = (-coefLin - math.sqrt(discriminante))/(2*coefCuad)
        print(f'Las raices son {r1:.2f} y {r2:.2f}')
        return None
    else:
        print('Las raices son numeros imaginarios lol')
        return None
    

#Aquí defino el proceso para la ecuacion normal
def despejeX():
    x = sp.symbols('x')
    lado_izq = input('Digite el lado izquierdo de la ecuacion: ')
    lado_der = input('Digite el lado derecho de la ecuacion: ')
    ecuacion = Eq(eval(lado_izq), eval(lado_der))
    solucion = solve(ecuacion, x)
    
    print(f'El despeje de X es: {solucion}')
    return None

#Aquí defino el proceso para las calificaciones promedio
def promedio(lista):
    suma = 0
    for numero in lista:
        suma = suma + numero
    return suma / len(lista)


apertura = int(input(print('Bienvenido a su calculadora de ecuaciones lineales y cuadraticas, digite que tipo \n' \
'de operación planea usar: \n' \
'1.- Ecuacion lineal \n' \
'2.- Ecuación cuadratica \n'
'3.- Promedio de calificaciones \n'
'R= ')))

if apertura == 1:
    despejeX()
elif apertura == 2:
    opcion = int(input(print('Digite que tipo de ecuacion cuadratrica usara:' \
    '1.Ax2 + Bx + C = 0' \
    '2.Ax2 + Bx = 0' \
    '3.Ax + C = 0 ')))
    if opcion == 1:
        ecuacion2Completa()
    elif opcion == 2:
        ecuacion2Mixta()
    else:
        ecuacion2Pura()
elif apertura == 3:
    cantidad_Cal = int(input('Digite la cantidad de materias que desea promediar: '))
    indice = 1
    lista_cal =[]
    while indice <= cantidad_Cal:
        lista_cal.append(int(input(f'Digite el promedio de su materia numero {indice}: ')))
        indice += 1
    print(f'Su promedio es {promedio(lista_cal)}')
    if promedio(lista_cal) > 70 and promedio(lista_cal) < 100:
        print('Su promedio es aprobatorio =)')
    elif promedio(lista_cal) < 70:
        diferencia = 70 - promedio(lista_cal)
        print(f'Su promedio es reprobatorio por {diferencia} puntos')
    elif promedio(lista_cal) > 100:
        print('Su promedio es irreal pues es mayor a 100, verifique sus calificaciones')




        
        
 
