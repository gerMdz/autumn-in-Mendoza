name = "Ger"
age = '55'
concat2 = f'MDZ {name}, {age}' #f-string
concat3 = 'MDZ {}, {}'.format(name, age) #format

print(concat2)
print(concat3)

print(f'String: {name} {age}')
print('Largo: {} y {}'.format( len(name),  len(age)))