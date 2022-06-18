"""
Autor: Pablo Lonardi
ing2i.py - creacion de una funcion que solicita el ingreso de 2 numeros enteros que luego almacenamos en variables
para luego realizar con ellos distintas operaciones.
"""

while True:                         #creamos un bucle para ejecutar un TRY en busca "SALVAR" ingresos no permitidos
    try:
        v1 = input("por favor ingresa un valor entero para N°1 ")  #solicito ingreso de primer valor
        val1 = int(v1)     #como el input es un string, lo convierto en entero para poder realizar operaciones
        break               #salimos del bucle si no hay errores
    except ValueError:
        print("el ingreso no es un numero entero") #en caso de error informo el mismo y vuelve a ingresar al bucle
          
while True:
    try:    
        val2 = int(input("por favor ingresa un valor entero para N°2 ")) #en este caso convierto en el mismo paso el input a valor entero
        break
    except ValueError:
        print("el ingreso no es un numero entero")
        
print("")                                                            #un poco de espacio para facilitar la lectura
print("los valores ingresados son los siguientes: ")
print("Valor 1 = " + str(val1)+"\n","Valor 2 = " +  str(val2), sep="")   #presentacion de los valores
print("")                                                                 #un poco de espacio para facilitar la lectura
