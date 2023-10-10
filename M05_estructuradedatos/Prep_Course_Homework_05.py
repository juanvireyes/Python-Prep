#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:
ciudades = ['Bogotá', 'Buenos Aires', 'Lima', 'CDMX', 'Santiago', 'Quito', 'Sao Pablo']
print(ciudades)



# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:
print(ciudades[1])



# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:
print(ciudades[1:4])




# 4) Visualizar el tipo de dato de la lista

# In[12]:
print(type(ciudades))




# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:
print(ciudades[2:])




# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:
print(ciudades[:4])


    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:
ciudades.append('Montevideo')
ciudades.append('Bogotá')
print(ciudades)
#No arroja ningun tipo de error pues una lista puede contener elementos repetidos





# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:
ciudades.insert(3, 'Asunción')
print(ciudades)



# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:
paises = ['Chile', 'Argentina', 'Uruguay']
ciudades.extend(paises)
print(ciudades)



# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:
print(ciudades.index('Montevideo'))
#Obtenemos el primer índice de la ciudad duplicada. Por ejemplo en este caso 'Montevideo' aparece 2 veces en el índice 8 y en el 10, pero el método index siempre va a retornar 8 que es el primer match que encuentra en la lista



# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:
# print(ciudades.index('Nashville'))
#El código de la línea 99 devuelve el error 'Nashville' no está en la lista






# 12) Eliminar un elemento de la lista

# In[25]:
ciudades.pop(9)
ciudades.pop(10)
ciudades.pop(11)
print(ciudades)




# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:
#ciudades.pop(15)
#print(ciudades)
#Se retorna un error de que el índice está fuera del rango de la lista porque sobrepasa la cantidad de elementos de la misma




# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:
last_city = ciudades[11]
print(last_city)




# 15) Mostrar la lista multiplicada por 4

# In[29]:
lista_multiplicada = ciudades * 4
print(lista_multiplicada)



# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:
lista = []
for n in range(1,21):
    lista.append(n)
tupla = tuple(lista)
print(tupla)



# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:
print(tupla[10:16])



# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:
print(20 in tupla)
print(30 in tupla)




# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:
city = 'París'
message = ''

if city in ciudades:
    message = 'La ciudad ' + city + ' ya existe'
else:
    ciudades.append(city)
    message = 'La ciudad ' + city + ' fue agregada'
print(message)



# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:
print(tupla.count(1))
print(ciudades.count('Montevideo'))




# 21) Convertir la tupla en una lista

# In[52]:
lista_2 = list(tupla)
print(lista_2)




# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:
tupla_2 = 1, 2, 3, 4, 5
num1, num2, num3 = tupla_2[:3]

print("Primer valor:", num1, "Segundo valor:", num2, "Tercer valor:", num3)





# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:
paises.append('Colombia')
paises.append('Perú')
paises.append('Brasil')
paises.append('Argentina')
paises.append('México')
paises.append('Ecuador')
paises.append('Paraguay')
diccionario = {
    'ciudad': ciudades,
    'paises': paises,
    'continente': ['América', 'America', 'América', 'América', 'América', 'América', 'América', 'América', 'América', 'América', 'América', 'América', 'Europa']
}

print(diccionario)





# 24) Imprimir las claves del diccionario

# In[59]:
paises.append('Francia')
print(diccionario.keys())



# 25) Imprimir las ciudades a través de su clave

# In[61]:
print(diccionario['ciudad'])




# %%
