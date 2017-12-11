def judge(q,m):
    for i in range(m):
        for j in range(i):
            if q[i] == q[j]:
                return 0
            elif q[i] == q[j] + i - j:
                return 0
            elif q[i] == q[j] + j - i:
                return 0

    return 1

def backtracking(q,i):
    global m2
    k = 1
    for j in range(8):
        q[i]=j
        if i != 0: #不为第一行，则判断当前可行性，不可行则回溯到上一层
            k = judge(q,i+1)
        if k == 1:
            if (i+1 != 8): #可行，则继续往下填充皇后
                backtracking(q,i+1)
            else: #若为最后一行，则计数+1
                m2+=1
                print(q)


m2 = 0
q = [[]]*8
backtracking(q,0)
print(m2)

