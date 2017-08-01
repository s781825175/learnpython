#输入一个数，把它按顺序插入一个已知序列中。
l = [1, 3, 4, 4, 5, 6, 6, 8, 65, 74] 
a = int(input('input a number:'))
s = len(l)
for i in range(s):
    if a<=l[i]:
        l.insert(i,a)
        break
    if a>l[-1]:
        l.append(a)
print (l)
