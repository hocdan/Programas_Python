'''
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to 
calculate the roots because a division by zero or a square root of a negative number, presents the 
message “Impossivel calcular”.

Input

Read 3 floating-point numbers (double) A, B and C.

Output

Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.

Examples:

10.0 20.1 5.1
	
R1 = -0.29788
R2 = -1.71212


0.0 20.0 5.0
	
Impossivel calcular


10.3 203.0 5.0
	
R1 = -0.02466
R2 = -19.68408


10.0 3.0 5.0
	
Impossivel calcular

'''
import math

coeficientes = input().split()
a = float(coeficientes[0])
b = float(coeficientes[1])
c = float(coeficientes[2])

delta = (b**2) - (4 * a * c)

if (delta < 0 or a == 0):
    print("Impossivel calcular")
elif (delta == 0):
    r1 = ( (b * -1) + math.sqrt(delta) ) / (2*a)
    r2 = r1
    print("R1 = {0:.5f}".format(r1))
    print("R2 = {0:.5f}".format(r2))
else:
    r1 = ( (b*-1) + math.sqrt(delta) ) / (2*a)
    r2 = ( (b*-1) - math.sqrt(delta) ) / (2*a)
    print("R1 = {0:.5f}".format(r1))
    print("R2 = {0:.5f}".format(r2))
