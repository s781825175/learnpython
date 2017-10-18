#! /user/bin/env python
#coding:utf-8

def lisint(lis):
    a=''
    for i in range(len(lis)):
        b=list(str(lis[0]))
        for j in b:
            lis.append(j)
        lis.pop(0)
    lis.sort()
    for i in lis:
        a+=i
    return int(a)

if __name__ == '__main__':
    lis=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,31,1,1,1,1,1,5,5,5,5,5,5,5,5,5,5,5,7]
    print(lisint(lis))
