def encaixa(numero_1, numero_2):
    return numero_1.endswith(numero_2)

N = int(input())

for _ in range(N):
    a, b = input().split()

    if encaixa(a, b):
        print("encaixa")
    else:
        print("nao encaixa")

