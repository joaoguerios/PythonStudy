lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def soma(x,y):
    return x+y

def juntar(l1,l2):
    indmin = (min(len(lista_a), len(lista_b)))
    return [(soma(l1[i],l2[i])) for i in range (indmin)]

print(juntar(lista_a,lista_b))
