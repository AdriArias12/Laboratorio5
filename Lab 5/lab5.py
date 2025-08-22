# Actividad 1

# Paso 1. Sintaxis basica y operaciones simples.

nombre1 = input("Ingrese su nombre:") #string
edad = int(input("Ingrese su edad:")) #int
estatura = float(input("Ingrese su estatura en metros:")) #float
es_estudiante = input("Es estudiante? (si/no):").lower() == "si" #boolean
adulto = edad>=18 #boolean
suma = edad + 5
multiplicacion = edad * 2

#Imprimir valores

print ("\n---Datos Ingresados---")
print ("Nombre:", nombre1)
print ("Edad:", edad)
print ("Estatura:", estatura)
print ("Es estudiante?", es_estudiante)
print ("Es adulto?", adulto)

print("En 5 años tendrás:", suma)
print("El doble de tu edad es:", multiplicacion)

# Concatenar cadenas de texto
mensaje = "Mi nombre es " + nombre1 + " y mido " + str(estatura) + " metros."
print(mensaje)

# Usar input() para recibir datos del usuario
nacimiento = input("¿Donde naciste?: ")
print("Yo naci en" + nacimiento)



# Paso 2. Condicionales y bucles
## Crear un script que pida al usuario un número y determine si es par o impar utilizando condicionales (if, else).

num2 = int(input("Ingresa un numero:"))

if num2 % 2==0:
    print("El numero es par")
else:
    print("El numero es impar")

## Implementar un bucle for para iterar sobre una lista de números e imprimir sus cuadrados.

numLista = [1,7,3,8,5]

for n in numLista:
    print("El cuadrado de", n, "es", n**2)

##  Usar un bucle while para solicitar repetidamente la entrada del usuario hasta que se cumpla una condición específica.
respuesta = ""

while respuesta != "no":
    print("Va a calcular el cuadrado de un numero que aun no esta en la lista?")
    numA= int(input("Ingresa un numero:"))
    numLista.append(numA)
    print("El numero cuadrado de", numA, "es", numA**2)
    respuesta = input("desea cacular el cuadrado de otro numero? (si/no):")
print ("Puedes continuar")


# Paso 3. Listas y Diccionarios (Preguntar)

#Lista de estudiantes
estudiantes=[]

#Diccionario de contactos
contactos={}

#Agregar estudiantes a la lista
respuesta = "si"
while respuesta == "si":
    nombre = input("Ingrese el nombre del estudiante: ")
    estudiantes.append(nombre)
    respuesta = input("¿Desea ingresar otro estudiante? (si/no): ")

print("\nLista de estudiantes:")
for est in estudiantes:
    print(est)

#Agregar contacto al diccionario
respuesta = "si"
while respuesta == "si":
    nombre = input("\nIngrese el nombre de la persona: ")
    correo = input("Ingrese el correo de la persona: ")
    contactos[nombre] = correo
    respuesta = input("¿Desea ingresar otro contacto? (si/no): ")

print("\nContactos guardados:")
for clave, valor in contactos.items():
    print(f"Nombre: {clave}, Correo: {valor}")

# Actualizar datos en el diccionario
respuesta = "si"
while respuesta == "si":
    nombre = input("\nIngrese el nombre del contacto a actualizar: ")
    if nombre in contactos:
        nuevo_correo = input("Ingrese el nuevo correo: ")
        contactos[nombre] = nuevo_correo
        print("Contacto actualizado.")
    else:
        print("Ese contacto no existe.")
    respuesta = input("¿Desea actualizar otro contacto? (si/no): ")

print("\nDiccionario final de contactos:")
for clave, valor in contactos.items():
    print(f"Nombre: {clave}, Correo: {valor}")



# Paso 4. Script de Resolución de Problemas Simples
## Calculadora

numero1 = float(input("\nIngrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print("\n--- Operaciones disponibles ---")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("\nElija una opción (1-4): ")

if opcion == "1":
    resultado = numero1 + numero2
    print("Resultado de la suma:", resultado)
elif opcion == "2":
    resultado = numero1 - numero2
    print("Resultado de la resta:", resultado)
elif opcion == "3":
    resultado = numero1 * numero2
    print("Resultado de la multiplicación:", resultado)
elif opcion == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado de la división:", resultado)
    else:
        print("No se puede dividir entre cero")
else:
    print("Opción no válida")
  
##Numero aleatorio (Funciona bien)

import random
nurandom = random.randint(1,20)

numAd = int(input("Ingresa un numero del 1 al 20:"))

while numAd != nurandom:
    if numAd < nurandom:
        print("El numero es mayor")
    else:
        print("El numero es menor")
        
    #Pedir otro intento
    numAd=int(input("Intenta con otro numero:"))
    
print("Ha adivinado el numero")
        
   