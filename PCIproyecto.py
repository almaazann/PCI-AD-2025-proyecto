#Aqui se realizara el proyecto de Pensamiento computacional 
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
    x = sp.symbols('x')   #Para más información de la función "Symbols()": https://docs.sympy.org/latest/modules/logic.html
    lado_izq = input('Digite el lado izquierdo de la ecuacion: ')
    lado_der = input('Digite el lado derecho de la ecuacion: ')
    ecuacion = Eq(eval(lado_izq), eval(lado_der)) #Para más informaciónd de la función "Eq()": https://docs.sympy.org/latest/explanation/gotchas.html#equals-signs
    solucion = solve(ecuacion, x)   #Para más información de la función "solve()": https://docs.sympy.org/latest/explanation/solve_output.html
    
    print(f'El despeje de X es: {solucion}')
    return None


#Aquí defino el proceso para las calificaciones promedio
def promedio(lista):
    suma = 0
    for numero in lista:
        suma = suma + numero
    return suma / len(lista)

#Aquí trabajo con vectores, calculo de magnitud 
def magnitud_Vector (vector):
    return math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)

#Aquí calculo su angulo 
def angulo_vec(vector1, vector2):
    vectores = [vector1, vector2]
    vecA = magnitud_Vector(vector1)
    vecB = magnitud_Vector(vector2)
    vecAB = producto_punto(vectores)
    return math.degrees(math.acos((vecAB / (vecA * vecB))))

#Aquí calculo el producto punto de vectores (producto escalar)
def producto_punto(vectores):
    return vectores[0][0]*vectores[1][0] + vectores[0][1]*vectores[1][1] + vectores[0][2]*vectores[1][2]

#Aquí el calculo del producto cruz de vectores (producto vectorial)
def producto_cruz(vectores):
    calculo_i =  vectores[0][1]*vectores[1][2] - vectores[0][2]*vectores[1][1]
    calculo_j = -1 * (vectores[0][0]*vectores[1][2] - vectores[0][2]*vectores[1][0])
    calculo_k = vectores[0][0]*vectores[1][1] - vectores[0][1]*vectores[1][0]
    result = [calculo_i, calculo_j, calculo_k]
    return result

#Aquí el calculo del producto cruz de vectores (producto escalar)
def triple_escalar(vectores):
    cruz = [vectores[0], vectores[1]]
    axb = producto_cruz(cruz)
    rc = [axb, vectores[2]]
    resultado = producto_punto(rc)
    return resultado



#Aquí inicio el menú de opciones
apertura = int(input('Bienvenido a su calculadora de ecuaciones lineales y cuadraticas, digite que tipo \n' \
'de operación planea usar: \n' \
'1.- Ecuacion lineal \n' \
'2.- Ecuación cuadratica \n'
'3.- Promedio de calificaciones \n' \
'4.- Trabajar con vectores\n' \
'R='))

if apertura == 1:
    despejeX()
elif apertura == 2:
    opcion = int(input('Digite que tipo de ecuacion cuadratrica usara:' \
    '1.Ax2 + Bx + C = 0' \
    '2.Ax2 + Bx = 0' \
    '3.Ax + C = 0 '))
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
elif apertura == 4:
    opcion = int(input('Que opciones desea usar?\n' \
    '1.-Magnitud de un vector\n' \
    '2.-Calcular el angulo entre 2 vectores\n' \
    '3.-Calcular el producto punto de 2 vectores\n' \
    '4.-Calcular el prodcuto cruz de 2 vectores\n' \
    '5.-Calcular el prodcuto triple escalar de 3 vectores \n' \
    'R='))
    if opcion == 1:
        vector = []
        print('Digite los componentes I, J y K de su vector')
        comp_i = float(input('I: '))
        comp_j = float(input('J: '))
        comp_k = float(input('K: '))
        vector = [comp_i, comp_j, comp_k]
        print(f'La magnitud de su vector {vector} es: {magnitud_Vector(vector)}')

    elif opcion == 2:
        print('Digite los componentes de su primer vector: ')
        comp_i = float(input('I: '))
        comp_j = float(input('J: '))
        comp_k = float(input('K: '))
        vector1 = [comp_i, comp_j, comp_k]
        print('Digite los componentes de su segundo vector: ')
        comp_i = float(input('I: '))
        comp_j = float(input('J: '))
        comp_k = float(input('K: '))
        vector2 = [comp_i, comp_j, comp_k]
        print(f'Su angulo (en grados) de los vectores {vector1} y {vector2} es: {angulo_vec(vector1, vector2):.2f}')


    elif opcion == 3:
        print('Digite los componentes de su primer vector: ')
        comp_i = float(input('I: '))
        comp_j = float(input('J: '))
        comp_k = float(input('K: '))
        vector1 = [comp_i, comp_j, comp_k]
        print('Digite los componentes de su segundo vector: ')
        comp_i = float(input('I: '))
        comp_j = float(input('J: '))
        comp_k = float(input('K: '))
        vector2 = [comp_i, comp_j, comp_k]
        vectores = [vector1, vector2]
        print(f'El producto escalar de los vectores {vector1} y {vector2} es: {producto_punto(vectores)}')

    elif opcion == 4:
        print('Digite los componentes de su primer vector: ')
        comp_i = float(input('I: '))
        comp_j = float(input('J: '))
        comp_k = float(input('K: '))
        vector1 = [comp_i, comp_j, comp_k]
        print('Digite los componentes de su segundo vector: ')
        comp_i = float(input('I: '))
        comp_j = float(input('J: '))
        comp_k = float(input('K: '))
        vector2 = [comp_i, comp_j, comp_k]
        vectores = [vector1,vector2]
        print((f'El resultado del prodcuto cruz de los vectores {vectores[0]}, {vectores[1]} es {producto_cruz(vectores)}'))

    elif opcion == 5:
        print('Digite los componentes de su primer vector: ')
        comp_i = float(input('I: '))
        comp_j = float(input('J: '))
        comp_k = float(input('K: '))
        vector1 = [comp_i, comp_j, comp_k]
        print('Digite los componentes de su segundo vector: ')
        comp_i = float(input('I: '))
        comp_j = float(input('J: '))
        comp_k = float(input('K: '))
        vector2 = [comp_i, comp_j, comp_k]
        print('Digite los componentes de su tercer vector: ')
        comp_i = float(input('I: '))
        comp_j = float(input('J: '))
        comp_k = float(input('K: '))
        vector3 = [comp_i, comp_j, comp_k]
        vectores = [vector1, vector2, vector3]
        print(f'El producto triple escalar de {vectores[0], vectores[1], vectores[2]} es igual a {triple_escalar(vectores)}')



else:
    print('Esa opcion no está dentro del menú, ejecute de nuevo')