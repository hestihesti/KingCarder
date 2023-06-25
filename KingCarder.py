import os
import sys
from termcolor import colored
import random
import datetime


month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
year = ['23', '24', '25', '26', '27', '28', '29']

# mastercard starts with 5
# visa starts with 4
# american express starts with 34 or 37
# discover starts with 6



try:
	number = 23
	second_num = 0
	start_digit = str(random.choice([34, 37, 4, 5, 6]))
	card_number = start_digit + ''.join(str(random.randint(0, 9)) for _ in range(15))

	cn = card_number
	cn2 = cn + '|'

	for i in range(1, 1000):
		with open('temp4.txt', 'a') as dub:
			for item1 in month:
					formm = f'{cn2}{item1}/'
					second_num += 1
					if second_num > 999:
						number += 1
						second_num = 1
					formmm = str(formm) + str(number) + '|'
					dub.write(str(formm) + str(number).zfill(2) + '|' + str(second_num).zfill(3) + '\n')



except:
	print('')


ques = input('What Would You Like To Name The File (include .txt):\n> ')
mv = 'mv temp4.txt ' + ques
mv2 = 'mv ' + ques + ' cards'
os.system(mv)
os.system(mv2)
