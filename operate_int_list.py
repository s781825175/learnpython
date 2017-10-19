import random

def operate_int_list(lis):
    return max(lis),min(lis),sum(lis),sum(lis)/len(lis)

if __name__ == '__main__':
    lis=[]
    for i in range(10):
        lis.append(random.randint(-100000000000000,100000000000000))
    print(operate_int_list(lis))
