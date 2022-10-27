import os
import sys
import time
from termcolor import colored

def Final():
	card = input('What Card Are You Testing: ')
	format = 'YES.txt'
	com = []
	format = 'yes.txt'
	if card == 'visa':
		with open(format, 'r') as fA:
			with open('CVV3.txt', 'r') as fB:
				with open('visa.txt', 'a') as fC:
					Alines = fA.readlines()
					Blines = fB.readlines()
					for i in range(len(Alines)):
						Line = Alines[i].strip() + '' + Blines[i]
						fC.writelines(Line)


	elif card == 'discover':
		with open(format, 'r') as fA:
			with open('CVV3.txt', 'r') as fB:
				with open('discover.txt', 'a') as fC:
					Alines = fA.readlines()
					Blines = fB.readlines()
					for i in range(len(Alines)):
						Line = Alines[i].strip() + '' + Blines[i]
						fC.writelines(Line)

	elif card == 'mastercard':
		with open(format, 'r') as fA:
			with open('CVV3.txt', 'r') as fB:
				with open('mastercard.txt', 'a') as fC:
					Alines = fA.readlines()
					Blines = fB.readlines()
					for i in range(len(Alines)):
						Line = Alines[i].strip() + '' + Blines[i]
						fC.writelines(Line)

	elif card == 'american_express':
		with open(format, 'r') as fA:
			with open('CVV3.txt', 'r') as fB:
				with open('american_express.txt', 'a') as fC:
					Alines = fA.readlines()
					Blines = fB.readlines()
					for i in range(len(Alines)):
						Line = Alines[i].strip() + '' + Blines[i]
						fC.writelines(Line)


	else:
		print('Invalid Input')

	rm4 = 'rm final.txt'
	os.system(rm4)
	rm5 = 'rm YES.txt'
	os.system(rm5)
	rm6 = 'rm yes.txt'
	os.system(rm6)


Final()
