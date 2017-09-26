def mam(li):
    a,b=None,None
    for i in li:
        if a == None:
            a,b=i,i
        if i > a:
            a=i
        if i < b:
            b=i
    return a,b

def fin(li):
    a=list(range(n))
    return sum(a)-sum(li)

def fibo(n):
    a,b=1,1
    for _ in range(n-2):
        a,b=a+b,a
    return a

def chess(x,y):
    if x%2==1 or y%2==1:
        return False
    else:
        return True

def virus(n):
    x,a=1,1
    while x<n:
        n-=x
        x,n=x*2,n*2
        a+=1
    return a

def chang(n,m,k):
    if (abs(n-m))%3==0 and k>=abs(n-m)/3:
        return True
    elif:(abs(n-k))%3==0 and m>=abs(n-k)/3:
        return True
    elif:(abs(m-k))%3==0 and n>=abs(m-k)/3:
        return True
    else:
        return False


        


    
