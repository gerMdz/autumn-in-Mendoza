# cadena a número

number_cadena = '55'
number_integer = int(number_cadena)
print(f'valor cadena de la cadena: {number_cadena}')
print(f'valor numérico de la cadena: {number_integer}')
print(f'valor numérico procesado: {number_integer / 5}')

print('##########')
number_cadena_1 = '3.1416'
number_float = float(number_cadena_1)
print(f'valor cadena de la cadena: {number_cadena_1}')
print(f'valor flotante de la cadena: {number_float}')
print(f'valor flotante procesado: {number_float * 10}')

print('##########')
number_entero = 65
number_cadena_2 = str(number_entero)
print(f'valor cadena de la cadena: {number_cadena_2}')
print(f'valor entero de la cadena: {number_entero}')
print(f'valor cadena procesado: {number_cadena} + 10')

print('##########')
cadena_bool_cero = 0
cadena_bool_null = ''
cadena_bool_none = None

print(f'valor cadena cero: {cadena_bool_cero}')
print(f'valor cadena null: {cadena_bool_null}')
print(f'valor cadena none: {cadena_bool_none}')

print('-_-_-_-_-_')
bool_cero = bool(cadena_bool_cero)
bool_null = bool(cadena_bool_null)
bool_none = bool(cadena_bool_none)

print(f'valor booleano cero: {bool_cero}')
print(f'valor booleano null: {bool_null}')
print(f'valor booleano none: {bool_none}')

print('-_-_-_-_-_')

cadena_bool_one = 1
cadena_bool_not_null = 'Algo'
cadena_bool_not_none = True

print(f'valor cadena uno: {cadena_bool_one}')
print(f'valor cadena not null: {cadena_bool_not_null}')
print(f'valor cadena not none: {cadena_bool_not_none}')

print('-_-_-_-_-_')
bool_one = bool(cadena_bool_one)
bool_not_null = bool(cadena_bool_not_null)
bool_not_none = bool(cadena_bool_not_none)

print(f'valor booleano cero: {bool_one}')
print(f'valor booleano null: {bool_not_null}')
print(f'valor booleano none: {bool_not_none}')

print('##########')

resultado_concatenado = number_cadena + number_cadena_1 + number_cadena_2
print(f'valor resultado concatenado: {resultado_concatenado}')

print('-_-_-_-_-_')
resultado_suma = number_integer + number_float + number_entero
print(f'valor resultado suma: {resultado_suma}')
