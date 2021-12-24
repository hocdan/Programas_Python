#crie tuplas
t1 = (1, 2, 3, 3, 2, 5)
t2 = (0,)
t3 = ()
print("Tupla 1: {}\nTupla 2: {}\nTupla 3: {}\n".format(t1, t2, t3))

#acesse o terceiro elemento desta tupla
tupla = (1, 2, 3, 4)
print(tupla[-1])

#unindo tuplas
print("ID da primeira tupla: {}".format(id(t1)))
print("ID da segunda tupla: {}".format(id(t2)))
t1 += t2
print(f"ID de t1 concatenada com t2: {id(t1)}")
print(t1)
