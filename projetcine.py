liste_film = []
continuer = 'o'

while continuer == 'o':
	nom_film = raw_input('Entrez votre nom de film: ')

	if nom_film.lower() in [film[0].lower() for film in liste_film]:
		print('le film {0} existe deja'.format(nom_film))
	else:
		note = raw_input('Entrez une note sur 5 pour ce film: ')
		liste_film.append((nom_film, note))
	continuer = raw_input('Voulez vous continuer ? o/n : ')
	print('')

liste_film.sort()
print(liste_film)