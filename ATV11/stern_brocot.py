def stern_brocot(m, n):

    numerador_esq, divisor_esq = 0, 1
    numerador_dir, divisor_dir = 1, 0
    
    resultado = []

    while True:

        numerador_nova_matriz = numerador_esq + numerador_dir
        divisor_nova_matriz = divisor_esq + divisor_dir

        if numerador_nova_matriz == m and divisor_nova_matriz == n:
            break

        if m * divisor_nova_matriz > n * numerador_nova_matriz:
            resultado.append('R')
            numerador_esq, divisor_esq = numerador_nova_matriz, divisor_nova_matriz

        else:
            resultado.append('L')
            numerador_dir, divisor_dir = numerador_nova_matriz, divisor_nova_matriz

    return ''.join(resultado)

while True:
    m, n = map(int, input().split())

    if m == 1 and n == 1:
        break

    print(stern_brocot(m, n))
