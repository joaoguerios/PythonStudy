# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
l1=['BA', 'SP', 'MG', 'RJ']
l2=['Salvador', 'Ubatuba', 'Belo Horizonte']

def juntar(l1,l2):
    menor = (min(len(l1), len(l2)))
    return [(l1[i],l2[i]) for i in range(menor)]

print(juntar(l1, l2))     

#ou

print(list(zip(l1,l2)))