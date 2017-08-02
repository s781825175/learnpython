def fact(n):
    return fact_iter(n, 1)


def fact_iter(n, a):
    if n==1:
        return a
    return fact_iter(n-1, n*a)

n=int(input("input a number:"))
a=fact(n)
print (a)
