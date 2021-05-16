n = int(input())
pontuacoes = input().split(" ")

pontuacoes2 = []
for ponto in pontuacoes:
    pontuacoes2.append(int(ponto))
pontuacoes2.sort()
segundo = pontuacoes2[0]
for i in range(len(pontuacoes2)-1, -1, -1):
    if pontuacoes2[i] < pontuacoes2[-1] and pontuacoes2[i] > segundo:
        segundo = pontuacoes2[i]
print(segundo)
