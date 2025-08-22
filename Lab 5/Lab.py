# Parte 1: Variables y Operaciones 

try:
    numero1 = int(input("\nIngrese el primer número entero: "))
    numero2 = float(input("Ingrese el segundo número decimal: "))
    
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

except Exception:
    print (f"Ingrese el numero con las condiciones solicitadas.")
    

#Parte 2: Listas 
frutas=["Pera", "Manzana", "Uva", "Banano", "Fresa"] 

respuesta = "si"
while respuesta == "si":
    fruta = input("Ingrese el nombre de la fruta: ")
    frutas.append(fruta)
    respuesta = input("¿Desea ingresar otra fruta? (si/no): ")

print("\nLista de frutas:")
for fruit in frutas:
    print(fruit)

# Parte 3: Diccionarios 
libros={}
respuesta = "si"
while respuesta == "si":
    titulo = input("\nIngrese el nombre del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    anoPublicacion = input("Ingrese el año de publicación: ")
    genero = input("Ingrese el género literario: ")
    libros[genero] = autor #Aqui defino como quiero que muestre la informacion
    respuesta = input("¿Desea ingresar otro libro? (si/no): ")
    
print("\nlibros guardados:")
for clave, valor in libros.items():
    print(f"Genero: {clave}, Autor: {valor}")

#Otra forma de hacer la parte 3

libro = {
    "Titulos":"",
    "Autores":"",
    "Años":0
    }

##Aqui estoy diciendo que la clave es genero
libro["Generos"]=""

print(libro)

libro["Titulos"]=input("Ingrese el nombre del libro: ")
libro["Autores"]=input("Ingrese el nombre del autor: ")
libro["Años"]=int(input("Ingrese el año de publicación: "))
libro["Generos"]=input("Ingrese el género literario: ")

print(libro) ##Imprime todo el diccionario


#Parte 4: Conjuntos 

##Asistencia del bootcamp
sesion20={2345, 8598, 9631, 4861, 4782, 2369}
sesion21={1234, 2345, 1225, 4861, 9874, 9836}

##Interseccion
interseccion=sesion20 & sesion21
print("Los asistentes a la sesion 20 y 21 fueron:", interseccion)

##Union (estuvo en una o en la otra)
union=sesion20 | sesion21
print("Los asistentes a una de las dos sesiones fueron:", union)

#Parte 5

numero_cadena=input("Ingrese un numero: ") #Cadena quiere decir que lo toma como un texto, todo lo que esta en comillas es texto
numero_entero=int(numero_cadena)  #Aqui convierto el texto a un entero

##validacion
suma=104+numero_entero

print("La suma de los numeros es:", suma)


#Prueba



