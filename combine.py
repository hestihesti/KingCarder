import os
import sys

def layers():
	i = 0
	c = input('What Card Are You Working With: ')
#	com = []
	while i < 2:
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
		with open('YES.txt', 'a') as fp:
			fp.write(data)
#		print(f'File Saved {i} Times!')

	rm = 'rm ' + c + '.txt'
	rm2 = 'rm ' + c + '2.txt'
	os.system(rm)
	os.system(rm2)


layers()

