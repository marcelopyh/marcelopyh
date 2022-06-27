lista = [] # 1, 2, 3, 4, 5 ... 10
for v in [1,2,3]:
    if v % 2 == 0:
        for b in [4,5,6]:
            lista.append((v,b))
print(lista)

lista2 = [(v,b) for v in [1,2,3] if v % 2 == 0 for b in [4,5,6] ] 
print(lista2)

lista3 = [ [i for i in range(4) ] for v in range(3) if v % 2 == 0 ]
print(lista3)

