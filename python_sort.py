#!/usr/bin/env python
#coding:utf-8

def quickSort(arr):
    less=[]
    pivotList=[]
    more=[]
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        print(less,more,pivot)

        return less+pivotList+more


if __name__ == '__main__':
    arr=[4, 65, 2, -31, 0, 99, 83, 782, 1]
    print(quickSort(arr))
