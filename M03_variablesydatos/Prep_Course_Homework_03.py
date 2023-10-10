#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla



# In[7]:
a = 3
print(a)



# 2) Imprimir el tipo de dato de la constante 8.5



# In[3]:
print(type(8.5))




# 3) Imprimir el tipo de dato de la variable creada en el punto 1



# In[8]:
print(type(a))




# 4) Crear una variable que contenga tu nombre

# In[2]:
name = "Juan Vicente Reyes"



# 5) Crear una variable que contenga un número complejo

# In[3]:

complex_number = 3 + 4j



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

print(type(complex_number))



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416
rounded_pi = round(pi, 4)


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

var_1 = 'True'
var_2 = True



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(var_1))
print(type(var_2))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
sum = 2 + 2.5
print(sum)




# 11) Realizar una operación de suma de números complejos

# In[2]:

complex_sum = complex_number + complex_number
print(complex_sum)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

sum_real_complex = complex_number + 2
print(sum_real_complex)



# 13) Realizar una operación de multiplicación

# In[5]:

multiply = 3 * 3

print(multiply)



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

b = 2**8
print(b)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

result = 27/4

print(result)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

result_2 = 27//4

print(result_2)

# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

result_3 = 27%4

print(result_3)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

sum = 6*4+3

print(sum)



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:


a = "Hola"
b = "Mundo"

c = a + b

print(c)




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

print("2" == 2) #Esto es falso debido a que el primer dos es un string y el segundo es un entero





# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

print(int("2") == 2)



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

#El error se encuentra en el hecho de que se está utilizando una coma para separar los decimales. La forma correcta es a = float('3.8')

d = float('3.8')

print(d)



# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

e = 3
e -= 1

print(e)




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

binary_num = 1 << 2

print(binary_num)

'''
El resultado es 4 porque, al tomar el sistema de numeración binario, el 1 se convierte en 0001 y el 2 indica el desplazamiento del primer dígito 1 dos posiciones 
a la izquierda por lo que el resultado será igual a 0100 que en el sistema de bits es igual al nùmero 4.
'''



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

'''
El resultado de 2 + '2' es un error debido a que el operador '+' no puede operar dos operandos de distinto tipo.
Si los dos operandos son del mismo tipo, el resultado variará dependiendo del tipo de dato que sea. Si son enteros, el resultado será 4.
Si los dos operandos son strings, el resultado será '22'.
'''
f_1 = 2
f_2 = '2'

f_3 = f_1 + int(f_2) #Se convierte el string '2' en un entero para poder realizar la operación. El resultado será 4.

print(f_3)

f_4 = str(f_1) + f_2 #Se convierte el entero 2 en un string para poder realizar la operación. El resultado será '22'.

print(f_4)




# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
dato_a = 3
dato_b = '3'

dato_c = dato_a + int(dato_b)
print(dato_c)




# %%
