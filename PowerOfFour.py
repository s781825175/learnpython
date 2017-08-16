import collections
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return bool(collections.Counter(bin(num))['1'] == 1 and 1431655764&num==num)

num=5
print(Solution().isPowerOfFour(num))
