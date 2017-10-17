def search(x,target):
    x.sort()
    while x[int(len(x)/2)]!=target:
        if x[int(len(x)/2)]<target:
            x=x[int((len(x)/2)):]
        else:
            x=x[:int((len(x)/2))]
        if len(x)==1:
            return False
    return True

if __name__ == '__main__':
    x=list(range(100))
    target=25
    print(search(x,target))

