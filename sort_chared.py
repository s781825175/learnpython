def sortchare(lis,char):
    num=list(range(len(char)))
    num_char=list(zip(char,num))
    num_lis=[]
    lis2=[]
    for i in lis:
        lis2.append(list(i))
    for i in lis2:
        a=[]
        for j in i:
            for k in range(len(num_char)):
                if j==num_char[k][0]:
                    a.append(num_char[k][1])
        num_lis.append(a)
    tot=list(zip(lis,num_lis))
    def by_char(tot):
        return tot[1]
    tot=sorted(tot,key=by_char)
    tot=list(zip(*tot))
    print(tot[0])

if __name__ == '__main__':
    char=['d', 'g', 'e', 'c', 'f', 'b', 'o', 'a']
    lis=["bed", "dog", "dear", "eye"]
    print(sortchare(lis,char))
