'''
You must make a program that read a float-point number and print a message saying in which of 
following intervals the number belongs: [0,25] (25,50], (50,75], (75,100]. If the read number 
is less than zero or greather than 100, the program must print the message “Fora de intervalo” 
that means "Out of Interval".

The symbol '(' represents greather than. For example:
[0,25] indicates numbers between 0 and 25.0000, including both.
(25,50] indicates numbers greather than 25 (25.00001) up to 50.0000000.

Input

The input file contains a floating-point number.

Output

The output must be a message like following example.

Examples:

25.01

Intervalo (25,50]


25.00
	
Intervalo [0,25]


100.00
	
Intervalo (75,100]


-25.02	

Fora de intervalo

'''
numero = float(input())

#checando o intervalo em que se encontra o numero
if ( numero < 0 or numero > 100):
    print("Fora de intervalo")
elif ( numero <= 25 ):
    print("Intervalo [0, 25]")
elif ( numero > 25 and numero <= 50):
    print("Intervalo (25, 50]")
elif ( numero > 50 and numero <= 75):
    print("Intervalo (50, 75]")
else:
    print("Intervalo (75, 100]")