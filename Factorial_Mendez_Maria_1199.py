#Entero positivo y Factorial
print(" ")
print ("pr_2_2do_Positivo-y-Factorial_Mendez_Sanchez_Maria_Guadalupe_Yazmin__3w_1199")
print(" ")
def factorial (n):                           #Definir Factorial
    if n == 0 or n == 1:                     #Si n es 0 o 1, el factorial es 1            
        resultado = 1                        #El resultado es 1
        #print(resultado)                     #Imprimir resultado
    elif n > 1:                              
        resultado = n * factorial (n-1)      #Llamada a la funcion
        #print(resultado)                     #Imprimir el resultado
    return resultado                         #Devover resultado final
    print("")
ress = factorial(10)                         #Hacerlo con el valor de 10
print("Imprime el factorial de 10:", ress)   #Imprimir el factorial de 10
print(" ")
