def fib(x):
    a=1
    b=1
    c=2
    while c!=x:
        a,b=a+b,a
        c+=1
    return a

if __name__ == '__main__':
    x=10
    print(fib(x))

