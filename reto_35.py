print('*** Reto 35 generar dirección de email a partir de variables ***')

name_user = 'Gerardo Julio Montivero '
name_business = "MPF MZA "
name_extension = "gob.ar"
print(name_user + "@" + name_business +'.' + name_extension)
print(f'Usuario: {name_user}')
name_user = name_user.strip().replace(' ', '.').lower()

print(f'Empresa: {name_business}')
name_business = name_business.replace(' ', '').lower()
print('Resultado:')
print(name_user + "@" + name_business +'.' + name_extension)
email = f'{name_user}@{name_business}.{name_extension}'
print(f'\n\t Resultado: {email}')

