'''exercicio de aumentar 10% o valor do produto usando modulo'''
import copy
from dados import produtos

print(*produtos, sep="\n")
print("---------------")
nova_lista = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
print(*nova_lista, sep="\n")
print('------------------------')

por_ordem = sorted(
    nova_lista, key=lambda p: p ["nome"])
print(*por_ordem,sep="\n")
print('------------------------')

por_ordem_inversa= sorted(
    nova_lista, key=lambda p: p["preco"],reverse=True
)
print(*por_ordem_inversa,sep="\n")
