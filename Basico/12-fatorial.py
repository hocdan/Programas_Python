def fatorial(n):
    if n <= 1:
        return 1
    else:
        return (n*fatorial(n-1))


n = int(input("Informe um numero N: "))

print("O fatorial de {} = {}...".format(n, fatorial(n)))
