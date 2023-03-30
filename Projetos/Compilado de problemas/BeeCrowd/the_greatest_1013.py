'''
Make a program that reads 3 integer values and present the greatest one followed by the message 
"eh o maior". Use the following formula:

MaiorAB = (a+b+abs(a-b)) / 2

Input

The input file contains 3 integer values.

Output

Print the greatest of these three values followed by a space and the message “eh o maior”.

EXAMPLE:

7 14 106
	
106 eh o maior

'''
import math

valores = input().split()

A = int(valores[0])
B = int(valores[1])
C = int(valores[2])

maiorAB = (A + B + abs(A-B)) / 2
maiorXC = (maiorAB + C + abs(maiorAB-C)) / 2

print("{} eh o maior".format(int(maiorXC)))