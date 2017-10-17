#! /usr/bin/env python
#coding:utf-8

def half_search(lst,target):
    lst.sort()
    a=0
    while lst[int(len(lst)/2)]!=target:
        if lst[(int(len(lst)/2))]<target:
            a+=(int(len(lst)/2))
            lst=lst[int(len(lst)/2):]
        if lst[int(len(lst)/2)]>target:
            lst=lst[:int(len(lst)/2)]
    a+=int(len(lst)/2)
    return a

if __name__ == '__main__':
    lst=list(range(100))
    target=50
    print(half_search(lst,target))
