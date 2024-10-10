print(" ")
print("pr_2_2do_string_Mendez_Sanchez_Maria_Guadalupe_Yazmin__3w_1199")
print(" ")
def longitud(texto):                             #Definir la longitud de texto
    palabras = texto.strip().split()             #Divide el texto y quita espacios al inicio y a final para leerlo mejor
    return len(palabras[-1]) if palabras else 0  #Retorna la longitud de la ultima palabra
texto = input("Introduce un texto: ")            #Pedir el texto
print(" ")
print("Longitud de la última palabra:", longitud(texto)) #Te dise cuantas letras tiene la ultima palabra
print(" ")