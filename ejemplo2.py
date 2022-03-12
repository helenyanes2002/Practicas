# numeros=[]

# tamaño = int(input("Ingresar el tamaño de la lista"))

# for i in range (tamaño):
#     numero=int(input("Ingrese numero"))
#     numeros.append(numero)
# print(numeros)

listaNumeros=[]

for i in range(0,5,1):
    numeroIngresado = int(input("Ingresar el número: "))
    listaNumeros.append(numeroIngresado)

buscarNumero = int(input("Qué número buscas?:"))
if(buscarNumero in buscarNumero):
    print("Si se encuentra en la lista")
else:
    print("No se encuentra en la lista")