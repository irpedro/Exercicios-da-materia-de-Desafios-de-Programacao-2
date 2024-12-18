def primo(n):

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def fermat(n):
    if primo(n):
        return False
    for i in range(2, n):
        if pow(i, n, n) != i:
            return False
    return True


while True:
    n = int(input())
    if n == 0:
        break
    if fermat(n):
        print(f"The number {n} is a Carmichael number.")
    else:
        print(f"{n} is normal.")

