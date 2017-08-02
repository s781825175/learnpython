def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        print(b)
        a, b = b, a+b
        n = n+1
    return a

m=int(input("input a number:"))
a=fib(m)
