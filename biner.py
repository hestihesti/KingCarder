import os
import sys
from termcolor import colored

def compiler():
	i = 0
	print(colored('IN  ALL  CAPS  TYPE  OUT  CARD', 'red'))
	c = input('What Card Are You Working With: ')
#   EDITED HERE ^ AND V
#	c = 'YES'
	while i < 9:
		i += 1
		data = data2 = ''
		form = c + '.txt'
		cpp = 'cp ' + c + '.txt' + ' ' + c + '2.txt'
		os.system(cpp)
		form2 = c + '2.txt'
		with open(form) as fp:
			data = fp.read()
		with open(form2) as fp:
			data2 = fp.read()
		data += ''
		data += data2
#			    v  edited here
		with open('YES.txt', 'a') as fp:
			fp.write(data)
		print(f'File Saved {i} Times!')

	rm = 'rm ' + c + '.txt'
	rm2 = 'rm ' + c + '2.txt'
	os.system(rm)
	os.system(rm2)
'''
def adder():
	com = []
	with open('YES.txt') as fa:
		with open('expire.txt') as fb:
			with open('VISA.txt', 'w') as fc:
				alines = fa.readlines()
				blines = fb.readlines()
				for i in range(len(alines)):
					line = alines[i].strip() + '' + blines[i]
					fc.write(line)

'''

compiler()

