def fibonacciseq(limite):
    sequencia = [0, 1]
    while True:
        valor = sequencia[-1] + sequencia[-2]
        if valor > limite:
            break
        sequencia.append(valor)
    return sequencia

def fibonaccinum(num):
    if num < 0:
        return False
    sequencia = fibonacciseq(num)
    return num in sequencia

def prin():
    try:
        num = int(input("Informe um número: "))
        if fibonaccinum(num):
            print(f"O número {num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

nome = 'teste'
if nome == "teste":
    prin()
