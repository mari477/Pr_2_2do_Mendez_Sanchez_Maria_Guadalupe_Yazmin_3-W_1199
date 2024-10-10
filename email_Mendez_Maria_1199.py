print(" ")
print("pr_2_2do_Email_Mendez_Sanchez_Maria_Guadalupe_Yazmin__3w_1199")
print(" ")
def es_email_valido(email):                           #Definir el email
    return '@' in email                               #Que se cumpla cuando este el @
email = input("Introduce tu dirección de email: ")    #Introducir el email
if es_email_valido(email):                            #Si laa direccion es valida 
    print("La dirección de email es válida.")         #Se cumple y pone el mensaje
else:                                                 #Si no  
    print("La dirección de email no es válida.")      #Salta y la pone como invalida
print(" ")