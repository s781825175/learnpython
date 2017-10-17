#!/usr/bin/env python
#coding:utf-8

def change_coin(target):
    coin=[1,2,5,10,20,50,100]
    coin=coin[::-1]
    num=0
    for i in coin:
        if target>=i:
            num+=target//i
            target=target%i
    if target==0:
        return num
    if target==1:
        return num+1

if __name__ == '__main__':
    target=19813
    print(change_coin(target))
