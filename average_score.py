#! /usr/bin python
#coding:utf-8

import random
score=[]
for _ in range(40):
    score.append(random.randint(0,100))
average=sum(score)/40
a=0
for i in score:
    if i<average:
        a+=1
print(sorted(score),a)
