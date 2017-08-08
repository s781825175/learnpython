#生成 20 个激活码
import random
l=list()
i=0
while i < 20:
    a=random.randint(100000, 999999)
    l.append(a)
    i+=1
print (l),
