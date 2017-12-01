def t12(coin,time):
    num = list(range(len(coin)))
    tot = zip(coin,num)
    tot = list(map(list,tot))
    tot = sorted(tot, key=lambda x:x[0])[::-1]
    if time < 3:
        a = tot[:2]
        b = [tot[0]]+[tot[2]]
        return max(a,b, key=lambda x:x[0])
    a=tot[:time]
    a=sorted(a, key=lambda x:x[1])
    b=list(range(time))
    c=[]
    for i in range(len(a)):
        c.append(a[i][1] - b[i])
    if len(list(set(c))) == 1:
        c = []
    else:
        c = []
        for i in range(len(a)):
            c.append(a[i][0])
        return sum(c)

    a = tot[:time-1]+[tot[time]]
    print(a)
    for i in range(len(a)):
        c.append(a[i][1] - b[i])
    if len(list(set(c))) != 1:
        c = []
        for i in range(len(a)):
            c.append(a[i][0])
        return sum(c)

    a = tot[:time-1] + [tot[time+1]]
    print(a)
    b = tot[:time-2] + tot[time-1:time+1]
    return max(a,b, key=lambda x:x[0])


coin = [6, 10, 13, 17, 12, 7]
time = 3
print(t12(coin,time))
