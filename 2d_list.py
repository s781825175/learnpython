#! /usr/bin/env python
#coding:utf-8
import random

def score(x):
    #type(x):list
    for _ in range(5):
        x.append(random.randint(0,100))
    return x
score1=[]
for _ in range(20):
    x=[]
    score(x)
    score1.append(x)
print(score1)
totle=[]
for i in score1:
    totle.append(sum(i))
print(totle)
average=[]
for k in range(5):
    a=0
    for j in range(20):
        a+=score1[j][k]
    average.append(a/20)
print(average)


