# Uses python3
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1

    a = 1
    b = 1
    c = a + b

    for i in range(2, n):
        # fib[i] = (fib[i-1] + fib[i-2]) % m
        c = (a + b)
        a = b
        b = c

    return c

n = int(input())
print(fibo(n))
