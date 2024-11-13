# Cadenas e índices
string_1 = 'Hola Ger'
string_2 = 'Bienvenido'
string_3 = '''Este es un curso de Python,
    hasta ahora extremadamente básico'''

print(string_1 + ', ' + string_2)
print()
print(string_3)
print()
print(string_1[0] + string_1[1] + string_1[2] + string_1[3])
print(string_1[5] + string_1[6] + string_1[7] )

# `len` toma el largo de una cadena. No se usa para enteros.
print(len(string_2))

#subcadenas

string_4 =string_3[0:10]
print(string_4)

string_5 =string_3[11:16]
print(string_5)

string_6 =string_3.find('Python')
print(string_6)

string_7 =len('Python')
string_8 = string_6 + string_7
string_9 =string_3[string_6:string_8]

print(string_7)
print(string_8)
print(string_9)
string_10 =string_3.replace('Python', 'PHP')
print(string_10)

# split transforma a lista, separa el string

string_11 = 'Gerardo, 55, Argentina'
string_12 = string_11.replace(' ','')
lista = string_12.split(',')
print(string_11)
print(lista)

