#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=18&codigo=18&inicio=15

'''Se debe crear y cargar una lista donde almacenar 5 sueldos. Desplazar el valor mayor de la lista a la última posición.
La primera aproximación para llegar en el próximo problema al ordenamiento completo de una lista tiene por objetivo analizar 
los intercambios de elementos dentro de la lista y dejar el mayor en la última posición.
El algoritmo consiste en comparar si la primera componente es mayor a la segunda, en caso que la condición sea verdadera, 
intercambiamos los contenidos de las componentes.'''

sueldos=[]
while len(sueldos)<5:
    valor=int(input("Ingrese un sueldo:"))
    sueldos.append(valor)
print("Lista sin desplazar el mayor al final:",sueldos)
aux=0
for x in range(4):
    if sueldos[x]>sueldos[x+1]:
        aux=sueldos[x]
        sueldos[x]=sueldos[x+1]
        sueldos[x+1]=aux
print("Lista desplazando el mayor al final:",sueldos)