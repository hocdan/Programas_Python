'''
Read the four values corresponding to the x and y axes of two points in the plane, p1 (x1, y1) and 
p2 (x2, y2) and calculate the distance between them, showing four decimal places after the comma, 
according to the formula:

Distance = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )

Input

The input file contains two lines of data. The first one contains two double values: x1 y1 and the 
second one also contains two double values with one digit after the decimal point: x2 y2.

Output

Calculate and print the distance value using the provided formula, with 4 digits after the decimal 
point.

EXAMPLE:

1.0 7.0
5.0 9.0
	
4.4721
'''
import math

point1 = input().split()
point2 = input().split()

distance = math.sqrt( pow((float(point2[0]) - float(point1[0])), 2) + pow((float(point2[1]) - float(point1[1])), 2) )

print("{0:.4f}".format(distance))