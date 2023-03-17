'''
PROBLEM 3: ROMAN TO INTEGER

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
'''

def roman_to_int(s: str) -> int:
        inteiro = 0

        #convertendo letras romanas em numeros arabes
        romano = []
        for letra in s:
            if letra == 'I':
                romano.append(1)
            elif letra == 'V':
                romano.append(5)
            elif letra == 'X':
                romano.append(10)
            elif letra == 'L':
                romano.append(50)
            elif letra == 'C':
                romano.append(100)
            elif letra == 'D':
                romano.append(500)
            elif letra == 'M':
                romano.append(1000)
            else:
                pass

        ignorar = False #flag para evitar somar o par subtraido
        #convertendo sequencia de numeros em um unico numero inteiro
        for x in range(len(romano)):
            if not ignorar:
                #realizando comparacao entre numero atual e proximo (caso houver)
                if (x+1 < len(romano)):
                    #verificando se ha um par para subtrair
                    if (romano[x] < romano[x+1]):
                        inteiro += (romano[x+1]-romano[x])
                        ignorar = True #numero x+1 nao precisa ser checado
                    else:
                        inteiro += romano[x]
                else:
                    inteiro += romano[x]
            else:
                ignorar = False
        return inteiro

romano1 = "III"
romano2 = "LVIII"
romano3 = "MCMXCIV"

print("A sequencia {} em romano equivale a {} em arabe.".format(romano1, roman_to_int(romano1)))
print("A sequencia {} em romano equivale a {} em arabe.".format(romano2, roman_to_int(romano2)))
print("A sequencia {} em romano equivale a {} em arabe.".format(romano3, roman_to_int(romano3)))
