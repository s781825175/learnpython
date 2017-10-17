#coding:utf-8

def even_odd(x):
    a,b=[],[]
    for i in x:
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    return a+b

if __name__ == '__main__':
    x=[7,9,12,5,4,9,8,3,12,89]
    print(even_odd(x))
