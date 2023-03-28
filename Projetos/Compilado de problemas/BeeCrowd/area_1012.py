'''
Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.

Input

The input file contains three double values with one digit after the decimal point.
Output

The output file must contain 5 lines of data. Each line corresponds to one of the areas described 
above, always with a corresponding message (in Portuguese) and one space between the two points and 
the value. The value calculated must be presented with 3 digits after the decimal point.

EXAMPLE:

3.0 4.0 5.2
	
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000

'''
DADOS = input().split()
A = float(DADOS[0])
B = float(DADOS[1])
C = float(DADOS[2])

#calculando area das diferentes formas geometricas com base nas dimensoes dadas
AREA_TRIANGLE = (A * C) / 2
AREA_CIRCLE = 3.14159 * (C**2)
AREA_TRAPEZIUM = ((A + B) * C) / 2 
AREA_SQUARE = B*B
AREA_RECTANGLE = A*B

#imprimindo resultados
print("TRIANGULO: {0:.3f}".format(AREA_TRIANGLE))
print("CIRCULO: {0:.3f}".format(AREA_CIRCLE))
print("TRAPEZIO: {0:.3f}".format(AREA_TRAPEZIUM))
print("QUADRADO: {0:.3f}".format(AREA_SQUARE))
print("RETANGULO: {0:.3f}".format(AREA_RECTANGLE))