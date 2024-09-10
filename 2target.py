def contar_vogais(texto):
    vogais = 'aA'
    contador = 0

    for caractere in texto:
        if caractere in vogais:
            contador += 1
    return contador

x = str(input('Escreva algo: '))
print(f"Quantidade da letras 'a' no texto: {contar_vogais(x)}")
