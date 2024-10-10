print(" ")
print("pr_2_2do_Escribir-Una-Funcion_Mendez_Sanchez_Maria_Guadalupe_Yazmin__3w_1199")
print(" ")
def suma(lista):                     #Definir la suma
    return sum(lista)                #Se cumple la suma
def multip(lista):                   #Definir la multiplicacion
    resultado = 1                    
    for num in lista:                #Para un numero de la lista
        resultado *= num             #Resultado  *= el numero
    return resultado                 #Se cumple el resultado
numeros = [10, 50, 2, 29]            #Numeros que se utilizran
print("La Suma es:", suma(numeros))        #Imprimir el resultado
print(" ")
print("La Multiplicación es:", multip(numeros)) #Imprimir el resultado
print(" ")