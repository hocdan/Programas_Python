'''
Write an algorithm that reads two floating values (x and y), which should represent the coordinates of
a point in a plane. Next, determine which quadrant the point belongs, or if you are at one of the 
Cartesian axes or the origin (x = y = 0).

If the point is at the origin, write the message "Origem".

If the point is at X axis write "Eixo X", else if the point is at Y axis write "Eixo Y".

Input

The input contains the coordinates of a point.

Output

The output should display the quadrant in which the point is.


Input Sample 	Output Sample

4.5 -2.2  -->  Q4

0.1 0.1  -->  Q1

0.0 0.0  -->  Origem

OBS:

Q1 => X e Y positivos
Q2 => X negativo e Y positivo
Q3 => X e Y negativos
Q4 => X positivo e Y negativo
'''
pontos = input().split()
pontoX = float(pontos[0])
pontoY = float(pontos[1])

#verificando se o ponto esta na origem, em um dos eixos ou em algum quadrante
if (pontoX == 0 and pontoY == 0):
    print("Origem")
elif (pontoX != 0 and pontoY == 0):
    print("Eixo X")
elif (pontoX == 0 and pontoY != 0):
    print("Eixo Y")
elif (pontoX > 0 and pontoY > 0):
    print("Q1")
elif (pontoX < 0 and pontoY > 0):
    print("Q2")
elif (pontoX < 0 and pontoY < 0):
    print("Q3")
elif (pontoX > 0 and pontoY < 0):
    print("Q4")