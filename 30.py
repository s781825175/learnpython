def stringcopy(s,n):
    t=[]
    s=list(s)
    for i in range(1,n+1):
        t.append(s[i])
    t=''.join(t)
    return t
