from random import randint
from itertools import combinations_with_replacement
import numpy as np
def genrnd():
  lista = []
  for i in range(50):
    a = randint(0,1000)
    lista.append(a)
  return lista
def suma_combinatoria(lista):
  suma=0
  posicion=0
  for i in lista:
    numero=i
    for j in lista[posicion:]:
      numero=j
      suma=suma+i+j
    posicion+=1
  return suma

def mul_combinatoria(lista):
  multi=1
  posicion=0
  for i in lista:
    numero=i
    for j in lista[posicion:]:
      numero=j
      multi=multi*i*j
    posicion+=1
  return multi


def sum_combinatoria(lista):
  resultado= 0
  combinatoria = combinations_with_replacement(lista, 2)
  for i in combinatoria:
    resultado=resultado+sum(i)
  return resultado

def multi_combinatoria(lista):
  resultado= 1
  combinatoria = combinations_with_replacement(lista, 2)
  for i in combinatoria:
    resultado=resultado*i[0]*i[1]
  return resultado

def media(lista):
  return sum(lista)/len(lista)
def mediana(lista):
  lista_ordenada=sorted(lista)
  mitad=len(lista)//2
  if len(lista_ordenada)%2:
    return (lista_ordenada[mitad])
  else:
    return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2.0

def minimo(lista):
  minimo=lista[0]
  for i in lista[1:]:
    if i<minimo:
      minimo=i
  return minimo

def maximo(lista):
  maximo=lista[0]
  for i in lista[1:]:
    if i>maximo:
      maximo=i
  return maximo

def rango(lista):
  return maximo(lista)-minimo(lista)

def varianza(lista):
  dif_cuadrado=0
  promedio=media(lista)
  for i in lista:
    dif_cuadrado=dif_cuadrado+(i-promedio)**2
  return dif_cuadrado/len(lista)



lista=genrnd()
print (suma_combinatoria(lista))
print (sum_combinatoria(lista))
print (mul_combinatoria(lista))
print (multi_combinatoria(lista))
print(media(lista))
print(np.mean(lista))
print(mediana(lista))
print(np.median(lista))
print (rango(lista))
print (np.amax(lista)-np.amin(lista))
print (varianza(lista))
print (np.var(lista))

