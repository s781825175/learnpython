#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5

a = int(input('input a number:'))
print (a,'=', end=' ')
while (a!=1):
    a=int(a)
    for i in range(2,a+1):
        if a%i==0 and a!=i:
            print (i,'*', end=' ')
            a=a/i
            break
        if a%i==0 and a==i:
            print (i, end=' ')
            a=1
