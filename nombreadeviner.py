from random import randint

nombre_a_deviner = randint(1, 100)
print(nombre_a_deviner)

premier_essai = input('Entrez votre premier essai: ')


resultat = nombre_a_deviner == premier_essai

print('Le resultat est ' + str(resultat))

premier_res = premier_essai > nombre_a_deviner

deuxieme_res = premier_essai < nombre_a_deviner

print(premier_res)
print(deuxieme_res)
