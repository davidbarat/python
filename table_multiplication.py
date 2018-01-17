continuer = 'o'

while continuer == 'o':
	nombre = raw_input('Entrez votre nombre: ')

	for i in range(1, 11):
 		print('{0} * {1} = {2}'.format(nombre, i, int(nombre) * i))

 	continuer = raw_input('Voulez vous continuer ? o/n')


print('Fin')