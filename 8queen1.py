n = 8
x = []
def text(x):
    if len(set(x)) < len(x):
        return 0
    a = list(range(len(x)))
    b,c=[],[]
    for i in range(len(x)):
        b.append(x[i]+a[i])
        c.append(x[i]-a[i])
    if len(set(b)) < len(b):
        return 0
    if len(set(c)) < len(c):
        return 0
    return 1
ori = 1
d = []

def queen(ori,x,d,n):
    if len(d) == 2:
        return d
    if len(x) == n: 
        if x not in d:
            d.append(x)
            if x[-1] < n:
                ori = x[-1]+1
                x.pop()
                print(ori,x,d)
                return queen(ori,x,d,n)
            else:
                ori = x[-2]+1
                x.pop()
                x.pop()
                return queen(ori,x,d,n)
        else:
            if x[-1] < n:
                ori = x[-1]+1
                x.pop()
                return queen(ori,x,d,n)
            else:
                ori = x[-2]+1
                x.pop()
                x.pop()
                return queen(ori,x,d,n)

    for i in range(ori,n+1):
        x.append(i)
        if text(x) == 1:
            return queen(1,x,d,n)
        else:
            x.pop()
    if x[-1] < n:
        ori = x[-1]+1
        x.pop()
    else:
        ori = x[-2]+1
        x.pop()
        x.pop()
    return queen(ori,x,d,n)

print(queen(ori,x,d,n))
