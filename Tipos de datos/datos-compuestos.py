#Datos que dentro tienen datos simples o mas datos compuestos

# Lista [] (Modificable)
lista = ["Marco Valadez","Marcouwu2",True,1.85]
# Tupla () (No modificable)
tupla = ("Marco Valadez","Marcouwu2",True,1.85)

lista[3] = "Makinola"

# TUPLA ES INMODIFICABLE
# clear
# tupla[3] = "Makinola" <------ Error

#print(lista[3])
#print(tupla[3])

# Conjunto {} (set) 

conjunto = {"Marco Valadez","Marcouwu2",True,1.8}
# Conjuntos son INNACCESIBLES al indice. Tampoco permite repetir valores dentro del conjunto
# print(conjunto[1])  <------ Error

# Diccionario (dict) Estructura es key + value
diccionario = {
    'nombre' : "Marco",
    'canal_de_twitch' : "Marcouwu2",
    'esta_feliz': True,
    'altura' : 1.84,
    'dato_duplicado': "Marco"
}

print(diccionario)