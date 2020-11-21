#Script que calcula la tabla de multiplicar de un numero

#solicitar numero al usuario por consola

numero = input('que numero quieres multiplicar?')

# el dato ingresado por el usuario es una cadena "<str>"
# se debe convertir a numero para poder multiplicar

numero = int(numero)

for n in range (10):

   r = numero * (n +1 )
   print(r)
