#IVA
print(" ")
print ("pr_2_2do_IVA_Mendez_Sanchez_Maria_Guadalupe_Yazmin_1199_3w")
print(" ")
def total_factura(cantidad, porcentaje_iva=21):                  #Definir el total de la factura
    return cantidad * (1 + porcentaje_iva / 100)                 #cantidad del porcentaje
cantidad = float(input("Introduce la cantidad sin IVA: "))       #Pedir la cantidad si iva
porcentaje = input("Introduce el porcentaje de IVA (dejar vacío para 21%): ")   #Pedir el iva
if porcentaje:
    total = total_factura(cantidad, float(porcentaje))   #Decir el total
else:
    total = total_factura(cantidad)                      #Total de la cantidad
print("El total de la factura es:", total)               #Decir el total
print(" ")
