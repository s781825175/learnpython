import collections
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return collections.Counter(bin(n))['1']

n=11
print(Solution().hammingWeight(n))
