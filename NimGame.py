class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n%4)
a=Solution()
n=4
b=a.canWinNim(n)
print(b)
