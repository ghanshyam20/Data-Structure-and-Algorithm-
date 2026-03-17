def fib(n):
    # base cases
    if n == 0:
        return 1
    if n == 1:
        return 1

    # start values
    a = 1
    b = 1

    i = 2

    # loop until n
    while i <= n:
        c = a + b
        a = b
        b = c
        i = i + 1

    return b