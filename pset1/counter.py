def prime(n):
    if n < 2:
        return False
    for d in range(2, n-1):
        if n % d == 0:
            return False
    return True

for n in range(1000):
    if prime(n) and not prime(6*n+1):
        print(f"{n} is a counter example")
        break
