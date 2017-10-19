#!/usr/bin/env python
#coding:utf-8


def count_element(one_list):
    return list(set(one_list))

one_list=[1,2,2,2,3,3,3,3,3]
print(count_element(one_list))
