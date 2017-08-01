#输出101到200中的所有素数

for i in range(101,201):
    for j in range(2,i-1):
        a=1
        if i%j==0:
            a=0
            break
    if a==1:
        print (i, end=' ')
