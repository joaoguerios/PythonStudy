#
frase = 'vida e auma caixa preta nunca saberemos o seu real significado'
cont = len(frase)
i = 0
letra_maIs_apareceu = ''
apareceu_vezes = 0
while i < cont:
    letra_atual = frase[i]
    letra_passada = frase[i-1]
    quantidade = frase.count(letra_atual)
    if quantidade > apareceu_vezes:
        letra_maIs_apareceu = letra_atual
        apareceu_vezes = quantidade
    i = i + 1
print(f'a letra que mais aparece foi "{letra_maIs_apareceu}" e aparece "{apareceu_vezes}" vezes')