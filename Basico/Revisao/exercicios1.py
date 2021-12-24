#mude o seguinte exemplo para usar o metodo f-string
name = "Mike"
age = 21
print("Hello %s! You are %i years old!\n" % (name, age))
print(f"Hello {name}! You are {age} years old!\n")

#concatene essas duas strings
string1 = "Meu nome é"
string2 = "Daniel"
print(string1 + string2)
print(' '.join([string1, string2]))

#use string slicing para conseguir a substring "is a" da seguinte string
string = "this is a string"
print(string[5:9])
