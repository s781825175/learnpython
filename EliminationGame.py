class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=list(range(1,n+1))
        while len(a)>1:
            a=a[1::2][::-1]
        return a

if __name__ == '__main__':
    n=9
    print(Solution().lastRemaining(n))
