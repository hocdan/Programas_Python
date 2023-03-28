'''


In this problem, the task is to read a code of a product 1, the number of units of product 1, the 
price for one unit of product 1, the code of a product 2, the number of units of product 2 and the 
price for one unit of product 2. After this, calculate and show the amount to be paid.

Input

The input file contains two lines of data. In each line there will be 3 values: two integers and a 
floating value with 2 digits after the decimal point.

Output

The output file must be a message like the following example where "Valor a pagar" means Value to Pay. 
Remember the space after ":" and after "R$" symbol. The value must be presented with 2 digits after 
the point.

Example:

12 1 5.30
16 2 5.10
	
VALOR A PAGAR: R$ 15.50

'''
#lendo e separando valores de entrada em valores unitarios
PRODUCT1 = input() 
PRODUCT1 = PRODUCT1.split()

PRODUCT2 = input()
PRODUCT2 = PRODUCT2.split()

#calculando com base nos dados coletados (que vao ser convertidos para seus valores numericos)
AMOUNT_TO_PAY = (float(PRODUCT1[2]) * int(PRODUCT1[1])) + (float(PRODUCT2[2]) * int(PRODUCT2[1]))

print("VALOR A PAGAR: R$ {0:.2f}".format(AMOUNT_TO_PAY))