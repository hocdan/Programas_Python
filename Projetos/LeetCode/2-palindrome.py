'''
PROBLEM 2: PALINDROME NUMBER

Given an integer x, return true if x is a
palindrome, and false otherwise.
'''

def isPalindrome( x: int) -> bool:
        numero = str(x)
        if (numero == numero[::-1]):
            return True
        else:
            return False

print("O numero 121 eh um palindromo?", isPalindrome(121))
print("O numero -121 eh um palindromo?", isPalindrome(-121))
print("O numero 10 eh um palindromo?", isPalindrome(10))

