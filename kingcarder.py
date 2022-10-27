import os
import sys
import time
from termcolor import colored

def king():

	step1 = 'python3 carder.py'
	step2 = 'python3 combine.py'
	step3 = 'python3 adder.py'
	step4 = 'python3 biner.py'
	step5 = 'python3 biner2.py'
	step6 = 'python3 ADHD.py'
	step7 = 'python3 ADHD2.py'


	os.system(step1)
	print(colored('Step 1 Completed', 'yellow'))

	os.system(step2)
	print(colored('Step 2 Completed', 'yellow'))
	
	os.system(step3)
	print(colored('Step 3 Completed', 'yellow'))
	
	os.system(step4)
	print(colored('Step 4 Completed', 'yellow'))
	
	os.system(step5)
	print(colored('Step 5 Completed', 'yellow'))

	os.system(step6)
	print(colored('Step 7 Completed', 'yellow'))

	os.system(step7)
	print(colored('Final Step Completed', 'green'))


	end = input('Clean Up, What Card Did You Choose: ')
	mv = 'cat ' + end + '.txt >> cards/' + end + '.txt'
	os.system(mv)
	print(colored('Final Results Are Saved In "cards"', 'cyan'))
	rmm = 'rm yes.txt'
	os.system(rmm)
	rmm2 = 'rm ' + end + '.txt'
	os.system(rmm2)

king()
