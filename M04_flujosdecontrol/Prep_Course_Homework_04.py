#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

a = 5

if a > 0:
    print("El número es mayor a cero")
else:
    print("El número es menor a cero")



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

a = "hola"
b = 4

if type(a) == type(b):
    print("Son del mismo tipo de dato")    
else:
    print("Son de tipos diferentes")



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for n in range(1,21):
    if n % 2 == 0:
        print(n, "es par")
    else:
        print(n, "es impar")



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for n in range(0,6):
    print('Valor: ', n, 'Número elevado a la potencia igual a 3: ', n**3)




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
b = 8
for n in range(1,b):
    print(n)




# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
n = 5
if(type(n) == int and n > 0):
    if(n > 0):
        factorial = n
        while(n > 2):
            n -= 1
            factorial *= n
        print('El factorial de', n, 'es', factorial)
    else:
        print('El número debe ser mayor a cero')
else:
    print('El número debe ser entero')



# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
m = 9
while(m > 2):
    m -= 1
    for n in range(1,m):
        print(n)




# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
n = 8
for i in range(1,n):
    while(n > 0):
        n -= 1
        print('Ciclo for número: ' + str(i))
        print('While número: ' + str(n))



# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
max_range = 30
n = 0
primo = True

while(n < max_range):
    for div in range(2,n):
        if n % div == 0:
            primo = False
    if primo:
        print(n)
    else:
        primo = True
    n += 1    



# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
n = 0
primo = True

while(n < max_range):
    for div in range(2,n):
        if n % div == 0:
            primo = False
            break
    if primo:
        print(n)
    else:
        primo = True
    n += 1




# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
ciclos_sin_break = 0
n = 0
primo = True
while (n < max_range):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))



# In[57]:
ciclos_con_break = 0
n = 0
primo = True
while (n < max_range):
    for div in range(2, n):
        ciclos_con_break += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')



# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
n = 300
while(n > 100):
    n -= 1
    if(n % 12 != 0):
        continue
    print(n)



# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
n = 1
sigue = 1
primo = True

while(sigue == 1):
    for div in range(2,n):
        if n % div == 0:
            primo = False
    if primo:
        print(n)
        input('¿Desea buscar el siguiente número primo? 1=Si, 0=No')
        if input() != '1':
            print('Fin de la búsqueda')
            break
    else:
        primo = True
    n += 1



# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

n = 300

while(n > 100):
    n -= 1
    if(n % 3 != 0 or n % 6 != 0):
        continue
    print(n)
    break




# %%
