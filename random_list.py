#!/usr/bin/env python
#coding:utf-8

import random

def random_list():
    a=[]
    b=[]
    for _ in range(100):
        a.append(random.randint(1000,9999))
    a_remainder = [i%10 for i in a]
    b = [a_remainder.count(i) for i in range(10)]
    print(a)
    print(b)

print(random_list())
