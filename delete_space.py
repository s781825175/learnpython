#! /usr/bin/env python
#coding:utf-8

def del_space(x):
    y=x.split('  ')
    x=' '.join(y)
    return x


if __name__ == '__main__':
    x='ashfouih  fasdf  sfo'
    print(del_space(x))
