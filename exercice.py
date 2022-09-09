#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return voltage*voltage/resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	o = v1[0]*v2[0]+v1[1]*v2[1]
	if (o == 0):
			return('true')
	else:
			return('false')

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	m = 0
	t = 0
	for v in values:
		if (0 <= v):
				m += v
				t += 1
	return (m/t)

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties = 0
	tens = 0
	fives = 0
	twos = 0
	ones = 0
	while value != 0:
		if value >= 20:
			twenties = twenties + 1
			value = value - 20
		elif value >= 10:
			tens = tens + 1
			value = value - 10
		elif value >= 5:
			fives = fives + 1
			value = value - 5
		elif value >= 1:
			ones = ones + 1
			value = value - 1

	print (twenties, tens, fives, twos, ones);

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		pass
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		pass
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
