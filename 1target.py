def fibo(num):
    sequencia = [0, 1]
    while True:
        valor = sequencia[-1] + sequencia[-2]
        if valor > num:
            break
        sequencia.append(valor)
    return sequencia
print(fibo(22))
