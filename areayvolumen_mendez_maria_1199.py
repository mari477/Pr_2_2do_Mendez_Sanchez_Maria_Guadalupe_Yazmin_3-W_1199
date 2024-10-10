print(" ")
print("pr_2_2do_AREA_VOLUME_Mendez_Sanchez_Maria_Guadalupe_Yazmin__3w_1199")
print(" ")
#Definir area de un circulo con formula
def area_circulo(radio):               
    pi = 3.1416                         
    area = pi * (radio ** 2)
    return area
#Definir el volumen de un circulo con todo y su formula
def volumen_circulo(radio):
    pi = 3.1416
    volumen = (4/3) * pi * (radio ** 3)
    return volumen
#Definir el volumen de un cilindro junto con su formula
def volumen_cilindro(radio, altura):
    pi = 3.1416
    volumen = pi * (radio ** 2) * altura
    return volumen
radio = float(input("Introduce el radio: "))                 #Pedir el radio
altura = float(input("Introduce la altura del cilindro: "))  #Pedir la altura del cilindro
print(" ")
print("Área del círculo:", area_circulo(radio))               #Imprimir el area del circulo
print("Volumen de la esfera:", volumen_circulo(radio))        #Imprimir el volumen de la esfera 
print("Volumen del cilindro:", volumen_cilindro(radio, altura)) #Imprimir el volumen del cilindro
print(" ")
