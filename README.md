# PCI-AD-2025-proyecto
Proyecto personal pensamiento computacional - Leonardo Antonio Almazán López - Ago-Dic 25
Contexto

Este proyecto va a consistir en una calculadora de multiples usos, entre ellos calcular el promedio de varias calificaciones, ecuaciones de primer y segundo grado.

Algoritmo - Calculadora de ecuaciones cuadráticas, ecuaciones normales, promedio de calificaciones y 
operaciones a partir de vectores

ENTRADAS:
-Pedir al usuario determinar si es una ecuacion de primer o segundo grado o si prefiere promediar sus calificaciones
-En caso de ser de primer grado, pedir al usuario como está escrita la ecuacion
-En caso de ser de segundo grado, pedir al usuario que forma tiene la ecuacion y pedir
los coeficientes
-En caso de ser promedio, pedir al usario cuantas calificaciones quiere promediar e invocar la función promedio
-En caso de ser operaciones de vectores, definir funciones para magnitud, angulo, producto punto, producto cruz y triple escalar

PROCESOS
0.-Definir las funciones para cada caso (reciclar variable) e importar librerias
1.-PEDIR si es ecuacion de primer o segundo grado
2.-SI es de primer grado:
    2.1.-PEDIR al usuario la forma en la que está escrita la ecuación
    2.2.-Llevar a cabo el calculo del despeje de X
    2.3.-MOSTRAR el valor de X
3.-SI es de segundo grado:
    3.1.-PEDIR al usuario la forma que tiene la ecuación (pura, mixta y completa.)
    3.2.-PEDIR al usuario los coeficientes
    3.3.-Llevar a cabo el calculo para el despeje de X
    3.4.-MOSTRAR el valor de las raíces
4.-SI es promedio de calificaciones: 
    4.1.-PEDIR al usuario la cantidad de calificaciones que quiere promediar (si son 2, 3 o 4 materias)
    4.2.-PEDIR al usuario cada calificacion
    4.3.-INVOCAR la función promedio y hacer el calculo
    4.4.-MOSTRAR el promedio
5.-SI es operación de vectores:
    5.1.-PEDIR que opcion utilizara, si magnitud, angulo, producto punto, producto cruz o triple escalar
        5.1.-SI la opcion es magnitud
            5.1.1.-SOLICITAR los componentes i,j y k de su vector
            5.1.2.-INVOCAR la funcion magnitud de vector
            5.1.3.-MOSTRAR el resultado
        5.2.-SI la opcion es angulo entre 2 vectores
            5.2.1.-PEDIR los componentes i,j y k de los vectores
            5.2.2.-INVOCAR la funcion de angulo entre 2 vectores
            5.2.3.-MOSTRAR el resultado
        5.3.-SI la opcion es producto punto entre 2 vectores
            5.3.1.-PEDIR los componentes i,j y k de los vectores
            5.3.2.-INVOCAR la funcion de producto punto entre 2 vectores
            5.3.3.-MOSTRAR el resultado
        5.4.-SI la opcion es producto cruz entre 2 vectores
            5.4.1.-PEDIR los componentes i,j y k de los vectores
            5.4.2.-INVOCAR la funcion de prodcuto cruz entre 2 vectores
            5.4.3.-MOSTRAR el resultado
        5.5.-SI la opcion es triple escalar entre 3 vectores
            5.5.1.-PEDIR los componentes i,j y k de los vectores
            5.5.2.-INVOCAR la funcion de triple escalar entre 3 vectores
            5.5.3.-MOSTRAR el resultado
6.-SINO
    6.1.-Solicitar que vuelva a ejecutar puesto no hay otra opcione
            
SALIDAS
Dependiendo el caso:
Valor de X o de las raíces/0's/X1 y x2
Promedio de calificaciones
Resultado de la operación de vectores

