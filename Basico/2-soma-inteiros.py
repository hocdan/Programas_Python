"""

Sum of Integers Up To n (integersums.py)

Write a function, add_it_up(), that takes a single integer as input and returns
the sum of the integers from zero to the input parameter.

The function should return 0 if a non-integer is passed in.

"""

def add_it_up(n):
    total = 0
    for i in range(0, n+1):
        total += i
    return total

num = int(input("Informe um numero: "))
soma = add_it_up(num)
print("A soma do intervalo entre 0 e {} = {}".format(num, soma))
