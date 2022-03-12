#Python. Lenguaje multiproposito: lógica, web, analista datos(IOT), IA 
#Interpretado -> editor de código/IDE 

#LISTAS DE DATOS(ARREGLOS)
#Datos del mismo tipo, en caso de lo contrario aplicar diccionario
#El nombre de la lista en plural 

ciudades=['Medallo', 'Cali', 'Bogota', 'Santa Marta', 'Cartagena']
print(ciudades)

#Esculcando la lista(mapear/recorrer/requisar/iterar) la lista
#Los auxiliares de un Foreach son variables locales
# Le agrega un elemento a lista(push) 

for ciudad in ciudades: 
    ciudad='medallo' 
print(ciudad)

#Arreglo / lista 2
numeros=[1,2,3,4,5]
suma1=0
suma2=0

for numero in numeros: 
    suma1+=1
    suma2+=numero
print(suma1, suma2)

multiplos=[1]

longitudLista = int(input("Ingresar el tamaño de la lista"))

for i in range (longitudLista):
    multiplos.append((i+1) * 7)
print(multiplos)






