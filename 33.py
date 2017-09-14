def cp(m,c):
    c=sorted(c)[::-1]
    t=[]
    for i in c:
        c,a=c%i,c//i
        t.append(a)
    return sum(t)
