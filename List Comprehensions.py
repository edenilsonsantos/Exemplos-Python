# obter os valores da tabuada
tb = [str(f'{i} x {j} = {i*j}') if j != 11 else '\n' for i in range(1,10) for j in range(1,12)]
for x in tb: print(x)

# obter os numeros pares da lista
l1 = [1,2,3,4,5,6] 
l2 = list(filter(lambda x: True if(x % 2 == 0) else False, l1))
l3 = [x for x in l1 if x % 2 == 0]
print(l2)
print(l3)

# varios ifs junto com for
l1 = list('abcdefghijk')
l2 = ['AA' if x == 'a' else 'BB' if x == 'b' else 'GG' if x == 'g' else x for x in l1]
print(l2)

# unir 2 listas e remover duplicados, manter ordem original    
l1 = [1,2,3,4,5,6]    
l2 = [6,5,4,7,8,9]
[l1.append(x) for x in l2 if x not in l1]
print(l1)

# remover duplicados da lista, manter ordem original
l3 = []
l4 = [6,5,4,7,8,9,6,5,4,1,2,3,3,2,1]
[l3.append(x) for x in l4 if x not in l3]
print(l3)

# remover duplicados, e ordenar os valores da lista 
l5 = []
l6 = [6,5,4,7,8,9,6,5,4,1,2,3,3,2,1]
l5 = list(set(l6))
print(l5)









