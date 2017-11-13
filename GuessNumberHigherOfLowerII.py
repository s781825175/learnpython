class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b=0,n
        num=0
        while a+1<b:
            a=int((n-a)/2)+a
            num+=a
        return num

if __name__ == '__main__':
    n=10
    print(Solution().getMoneyAmount(n))
