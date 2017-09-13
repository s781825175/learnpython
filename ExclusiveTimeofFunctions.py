class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        a,b,c=[],[],[]
        for i in logs:
            n,typ,end=i.split(':')
            n,end=int(n),int(end)
            if typ == 'start':
                a.append(end)
            if typ == 'end':
                b.append(end)
        b=b[::-1]
        for i in range(len(a)):
            c.append(b[i]-a[i]+1)
        for i in range(len(c)):
            if i+1==len(c):
                break
            c[i]=c[i]-sum(c[i+1:])
        return c



if __name__ == '__main__':
    n=2
    logs =["0:start:0","1:start:2","1:end:5","0:end:6"]
    print(Solution().exclusiveTime(n,logs))
