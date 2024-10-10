print(" ")
print("pr_2_2do_Distancia-Dirigida_Mendez_Sanchez_Maria_Guadalupe_Yazmin__3w_1199")
print(" ")
def distancia_dirigida(x1, y1, x2, y2):                #Definir la distacia recorrida
    return (x2 - x1, y2 - y1)                          #Que se cumpla la codicion
x1, y1 = map(float, input("Introduce las coordenadas del primer punto (x1 y1): ").split())    #Pedir las cordenadas
x2, y2 = map(float, input("Introduce las coordenadas del segundo punto (x2 y2): ").split())   #Pedir cordenadas
print(" ")
distancia = distancia_dirigida(x1, y1, x2, y2)               #Definir distancia
print("La distancia dirigida es:", distancia)                #Imprimir la distacia que es
print(" ")
