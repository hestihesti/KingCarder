import os
import sys

card = input('What Card Are You Testing: ')
format = 'YES.txt'
com = []
def SeaVs():
	com = []
	format = 'yes.txt'
	if card == 'visa':
		with open(format, 'r') as fa:
			with open('CVV2.txt', 'r') as fb:
				with open('visa.txt','a') as fc:
					alines = fa.readlines()
					blines = fb.readlines()
					for i in range(len(alines)):
						line = alines[i].strip() + '' + blines[i]
						fc.writelines(line)

	elif card == 'discover':
		with open(format, 'r') as fa:
			with open('CVV2.txt', 'r') as fb:
				with open('discover.txt', 'a') as fc:
					alines = fa.readlines()
					blines = fb.readlines()
					for i in range(len(alines)):
						line = alines[i].strip() + '' + blines[i]
						fc.writelines(line)


	elif card == 'mastercard':
		with open(format, 'r') as fa:
			with open('CVV2.txt', 'r') as fb:
				with open('mastercard.txt', 'a') as fc:
					alines = fa.readlines()
					blines = fb.readlines()
					for i in range(len(alines)):
						line = alines[i].strip() + '' + blines[i]
						fc.writelines(line)
#					mv = "mv '~MASTERCARD~.txt' cards/Fullz/"
#					os.system(mv)

	elif card == 'american_express':
		with open(format,'r') as fa:
			with open('CVV2.txt', 'r') as fb:
				with open('american_express.txt', 'a') as fc:
					alines = fa.readlines()
					blines = fb.readlines()
					for i in range(len(alines)):
						line = alines[i].strip() + '' + blines[i]
						fc.writelines(line)
#					mv = "mv '~AMERICAN_EXPRESS~.txt' cards/Fullz/"
#					os.system(mv)


	else:
		print('Invalid Input')

SeaVs()
