#! /usr/bin/env python
#coding:utf-8

def merge_sort(lst):
    s=-2
    for i in range(1,(len(lst)//4)+1):
        a=lst[:(s+i*4)]
        b=lst[(s+i*4):i*4]
        a.sort()
        b.sort()
        c=[]
        while len(a)!=0 and len(b)!=0:
            if a[0]>=b[0]:
                c.append(b[0])
                b.pop(0)
            else:
                c.append(a[0])
                a.pop(0)
        if len(b)!=0:
            c+=b
        else:
            c+=a
    for i in lst[(len(lst)-len(lst)%4):]:
        for j in range(len(c)):
            if j==len(c)-1:
                c.append(i)
            if i>c[j] and i<c[j+1]:
                c.insert(j+1,i)
    return c

if __name__ == '__main__':
    lst=[6,2,3,1,7,43,6324,52,23,5,234,8,9,14]
    print(merge_sort(lst))
