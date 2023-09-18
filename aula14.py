#kgkgckg
def multiplicar(*args):
    total = 1
    for numero in args:
        total += numero * total
    return total

def parimpar(total):
    if total % 2 == 0:
        print(f'o numero {total} eh par')
    else:
        print(f'o numero {total} eh impar')

total = multiplicar(1, 2, 3, 4, 5)
parimpar(total)
