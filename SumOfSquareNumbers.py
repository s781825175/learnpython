import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        c=int(c)
        for a in range(1,int(math.sqrt(c))):
            b=c-a*a
            if len(list(str(math.sqrt(b))))==3:
                return True
        return False
c=input()
print(Solution().judgeSquareSum(c))
