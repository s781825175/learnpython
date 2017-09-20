import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        for i in range(1,9):
            print( math.factorial(i))

m=3
n=7
print(Solution().uniquePaths(m,n))
