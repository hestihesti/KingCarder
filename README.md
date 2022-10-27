This program generates a credit cards 16 digit number (visa starts with 4, mastercard starts with 5, discover starts with 6, and 
american express starts with 34 or 37). The rest of the numbers are set randomly. Once 16-digit is created it multiplies itself by 6,
so now you have 6 copies of the same card. Once that is done, it multiplies itself again by 2 and attaches the expiration date at the 
end of it. now some serious math happends that allows a cvv '001' to be passed through each expiration date. After the expiration date 
hits december, it restarts, but the cvv goes up by '001'. So now the code is passing '002' in for the cvv. This program works with a 2 year 
span, but it can be modified in "adder.py". The program saves the file in the 'cards' Directory. Now all you need to do is get yourself a 
CreditCardChecker/CreditCardVerifier and a CreditCardInformationOSINT type thing them you'll have yourself one hell of a setup.

			BE SAFE
		USE TOR, VPN, AND PROXIES
	
______________________________________________________________________________________________________________________________________________
______________________________________________________________________________________________________________________________________________

#		TO RUN THE PROGRAM

- pip3 install termcolor
- python3 kingcarder.py


		YOU WILL NEED TO TYPE OUT THE CARD YOU ARE MAKING MULTIPLE TIMES

1.	visa/mastercard/discover/american express
2.	press [q] to continue running without making more cards
3.	visa/mastercard/discover/american_express
4.	visa/mastercard/discover/american_express
5.	VISA/MASTERCARD/DISCOVER/AMERICAN_EXPRESS
6.	visa/mastercard/discover/american express
7.	visa/mastercard/discover/american express
8.	visa/mastercard/discover/american express

_________________________________________________________________________________________________________________________________


#		If You Want To Run The Program By Individual Programs Do The Following


1. 'python3 carder.py'
	choose card type
>	this creates 6 copies of that card number

2. 'python3 combine.py'
	choose card you just did
>	this multiplies that number 2 times (multiplying 12x5 to make 5 years)

3. 'python3 adder.py'
	choose card again
>	this factors in the dates in with the card number

4. 'python3 biner.py'
	choose card again..
>	must do

5. 'python3 biner2.py'
>	this allows makes it so you can add the CVV's to the card and expire date

6. 'python3 ADHD.py'
	choose card for last time
>	this places 500 CVV's in with the expiration date and card number


7. 'python3 ADHD2.py'
>	this places the other 499 CVV's in with the cc and expire date
_________________________________________________________________________________________________________________________
__________________________________________________________________________________________________________________________

#	IF YOU WANT TO CHANGE THE DATE FROM THE PROGRAMS DEFAULT SETTING...
>		1. open "adder.py" in your text editor
>			2. go to the variale "date"
>				3. change expire.txt to...
#					expire2.txt
					    OR
#					expire3.txt

	I only have dates going up to January/2023-December/2028 configured. They are divided up by 2's in the EXPIRE text files.
