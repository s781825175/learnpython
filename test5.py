#题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数。

for i in range(1,1001):
    a=0
    for j in range(1,i+1):
        if i%j==0 and i>j:
            a+=j
    if i==a:
        print (i)

