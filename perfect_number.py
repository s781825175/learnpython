#!/usr/bin/env python
#coding:utf-8

def perfect_number():
    a=[]
    for i in range(2,10000):
        b=[]
        for j in range(1,i):
            if i%j==0:
                b.append(j)
        if sum(b)==i:
            a.append(i)
    return a 

print(perfect_number())
