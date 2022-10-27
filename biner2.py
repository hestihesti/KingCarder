from termcolor import colored
import os
import sys


def test():
	i = 0
	print(colored('IN  ALL  CAPS  TYPE  OUT  CARD', 'yellow'))
#	c = input('What Card Are You Working With: ')
	c = 'YES'
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
		with open('yes.txt', 'a') as fp:
			fp.write(data)
		print(f'File Saved {i} Times!')

	rm = 'rm YES.txt'
	rm2 = 'rm YES2.txt'
	os.system(rm)
	os.system(rm2)


test()
