#Creando tuplas en python 
#Solo no puedo cambiar el tamaño es la única diferencia 
estudiantes=('Carlos', 'Juan Carlos')
print(estudiantes)

#estudiantes.append('martha') ERROR NO SE PUEDE
#print(estudiantes)
#Un diccionario no se escribe en plural

#Recorriendo tuplas
for estudiante in estudiantes:
        print(estudiantes)

#Convertir tupla en lista
listaEstudiantes=list(estudiantes)
print(listaEstudiantes)

#El diccionario de datos no es más que un objeto, este se escribe en singular apesar de que contengan varios datos

estudiante={
        'nombre':'Falcao',
        'edad':34,
        'esFutbolista':True
} 

#Imprimir/acceder a todas las llaves 
#atributos de mi diccionario 
print(estudiante)
#Necesito acceder a un atributo o llave del diccionario 
print(estudiante['nombre'])
print(estudiante.get('edad'))

#Recorrer un diccionario y obtener sus valores 
#y obtener sus valores 
for valor in estudiante.values():
        print(valor)