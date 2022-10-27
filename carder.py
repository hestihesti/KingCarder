import sys
import os
from termcolor import colored
import random
import time

#q1 = ''
def genr():
	q1 = 0
	cc = input(colored('Type Of Card (visa, mastercard, american_express, and discover):   ', 'magenta'))



	while q1 != 'q':
#		VISA

		if cc == 'visa':
			set = [4]
			for i in range(0,15):
				n = random.randint(0,9)
				set.append(n)

			form = f'{set}|\n'
			action = form * 6

			with open('cards.txt', 'a') as f:
				f.write(action)

			with open(r'cards.txt', 'r') as infile, \
				open(r'Cards.txt', 'w') as outfile:
				data = infile.read()
				data = data.replace(",", "")
				data = data.replace(" ", "")
				data = data.replace("[", "")
				data = data.replace("]", "")
				outfile.write(data)

			with open('Cards.txt', 'r') as fin:
				dat = fin.read().splitlines(True)
			with open('CC.txt', 'w') as fout:
				fout.writelines(dat[:15])
#			print('File Is Created')

			append = 'cat CC.txt >> visa.txt'
			rm_c = 'rm cards.txt'
			rm_C = 'rm Cards.txt'
			rm_CC = 'rm CC.txt'
			catt = 'cat visa.txt'

			os.system(append)
			os.system(rm_c)
			os.system(rm_C)
			os.system(rm_CC)
			os.system(catt)

			q1 = input(colored('[c]ontinue or [q]uit: ', 'yellow'))

#		MASTERCARD
		if cc == 'mastercard':
			set = [5]
			for i in range(0,15):
				n = random.randint(0,9)
				set.append(n)
				form = f'{set}|\n'
				action = form * 6

				with open('cards.txt', 'w') as f:
					f.write(action)

				with open(r'cards.txt', 'r') as infile, \
					open(r'Cards.txt', 'w') as outfile:
					data = infile.read()
					data = data.replace(",", "")
					data = data.replace(" ", "")
					data = data.replace("[", "")
					data = data.replace("]", "")
					outfile.write(data)

				with open('Cards.txt', 'r') as fin:
					dat = fin.read().splitlines(True)
				with open('CC.txt', 'w') as fout:
					fout.writelines(dat[:15])

#			print('File Is Created')

			append = 'cat CC.txt >> mastercard.txt'
			rm_c = 'rm cards.txt'
			rm_C = 'rm Cards.txt'
			rm_CC = 'rm CC.txt'
			cat = 'cat mastercard.txt'

			os.system(append)
			os.system(rm_c)
			os.system(rm_C)
			os.system(rm_CC)
			os.system(cat)

			q1 = input(colored('[c]ontinue or [q]uit: ', 'yellow'))

#			american express
		if cc == 'american_express':
			set = [34]
			set2 = [37]
			for i in range(0,14):
				n = random.randint(0,9)
				set.append(n)
				form = f'{set}|\n'
				action = form * 6

				with open('cards.txt', 'w') as f:
					f.write(action)

				with open(r'cards.txt', 'r') as infile, \
					open(r'Cards.txt', 'w') as outfile:
					data = infile.read()
					data = data.replace(",", "")
					data = data.replace(" ", "")
					data = data.replace("[", "")
					data = data.replace("]", "")
					outfile.write(data)

				with open('Cards.txt', 'r') as fin:
					dat = fin.read().splitlines(True)
				with open('CC.txt', 'w') as fout:
					fout.writelines(dat[:15])

#			print('File Is Created')
			append = 'cat CC.txt >> american_express.txt'
			rm_c = 'rm cards.txt'
			rm_C = 'rm Cards.txt'
			rm_CC = 'rm CC.txt'
			cat = 'cat american_express.txt'

			os.system(append)
			os.system(rm_c)
			os.system(rm_C)
			os.system(rm_CC)
			os.system(cat)

			q1 = input(colored('[c]ontinue or [q]uit: ', 'yellow'))
#		DISCOVER
		if cc == 'discover':
			set = [6]
			for i in range(0,15):
				n = random.randint(0,9)
				set.append(n)
				form = f'{set}|\n'
				action = form * 6

				with open('cards.txt', 'w') as f:
					f.write(action)

				with open(r'cards.txt', 'r') as infile, \
					open(r'Cards.txt', 'w') as outfile:
					data = infile.read()
					data = data.replace(",", "")
					data = data.replace(" ", "")
					data = data.replace("[", "")
					data = data.replace("]", "")
					outfile.write(data)

				with open('Cards.txt', 'r') as fin:
					dat = fin.read().splitlines(True)
				with open('CC.txt', 'w') as fout:
					fout.writelines(dat[:15])

#			print('File Is Created')

			append = 'cat CC.txt >> discover.txt'
			rm_c = 'rm cards.txt'
			rm_C = 'rm Cards.txt'
			rm_CC = 'rm CC.txt'
			cat = 'cat discover.txt'

			os.system(append)
			os.system(rm_c)
			os.system(rm_C)
			os.system(rm_CC)
			os.system(cat)


			q1 = input(colored('[c]ontinue OR [q]uit: ', 'yellow'))
		elif q1 == 'q':
			break
		else:
			print('Invalid Input')

genr()

