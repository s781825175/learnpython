#一个数+100是一个完全平方数，再+168也是一个完全平方数，求这个数

for i in range(1,10000):
    for j in range(1,100):
        for k in range(j,j+13):
            a=j*j
            b=k*k
            if i+100==a and i+268==b:
                print i
