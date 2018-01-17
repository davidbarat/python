from random import randint

nombre_de_coup = 5
nombre_a_deviner = randint(1, 100)


while nombre_de_coup != 0:

	essai = input('Entrez votre nombre: ')

	if essai == nombre_a_deviner:
		print('Vous avez gagne en {0}'.format(nombre_de_coup))
		break

	elif essai < nombre_a_deviner:
		print('le nombre a deviner est plus grand que ' + str(essai))
	else:
		print('le nombre a deviner est plus petit que ' + str(essai))

	nombre_de_coup-=1
	print('Il vous reste {0} essai'.format(nombre_de_coup))


if essai != nombre_a_deviner:
	print('You loose')
	print('Le nombre a deviner etait : ' + str(nombre_a_deviner))

print('Fin du jeu')




