def uscp(m):
    m,q=m%25,m//25
    m,d=m%10,m//10
    m,n=m%5,m//5
    return q+d+n+m

