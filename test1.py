#题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少

lis = []
c = 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            if i!=j and j!=k and k!=i:
                c = i*100+j*10+k
                lis.append(c)
print lis

