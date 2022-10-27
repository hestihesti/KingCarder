import os
import sys
from termcolor import colored

card = input('What Card Are You Testing: ')
com = []
def addEm():
	com = []
	format = 'YES.txt'

#		v Change Date Here If Desired
#			{expire2.txt} OR {expire3.txt}
	date = 'expire.txt'

		#	VISA
	if card == 'visa':
		with open(format, 'r') as fa:
			with open(date, 'r') as fb:
				with open('VISA.txt','w') as fc:
					alines = fa.readlines()
					blines = fb.readlines()
					for i in range(len(alines)):
						line = alines[i].strip() + '' + blines[i]
						fc.write(line)

		#	DISCOVER
	elif card == 'discover':
		with open(format, 'r') as fa:
			with open(date, 'r') as fb:
				with open('DISCOVER.txt', 'w') as fc:
					alines = fa.readlines()
					blines = fb.readlines()
					for i in range(len(alines)):
						line = alines[i].strip() + '' + blines[i]
						fc.write(line)


		#	MASTERCARD
	elif card == 'mastercard':
		with open(format, 'r') as fa:
			with open(date, 'r') as fb:
				with open('MASTERCARD.txt', 'w') as fc:
					alines = fa.readlines()
					blines = fb.readlines()
					for i in range(len(alines)):
						line = alines[i].strip() + '' + blines[i]
						fc.write(line)



		#	AMERICAN EXPRESS
	elif card == 'american_express':
		with open(format,'r') as fa:
			with open(date, 'r') as fb:
				with open('AMERICAN_EXPRESS.txt', 'w') as fc:
					alines = fa.readlines()
					blines = fb.readlines()
					for i in range(len(alines)):
						line = alines[i].strip() + '' + blines[i]
						fc.write(line)



	else:
		print('Invalid Input')


	rm4 = 'rm final.txt'
	os.system(rm4)
	rm5 = 'rm YES.txt'
	os.system(rm5)


addEm()
