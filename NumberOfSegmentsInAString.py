import collections
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return collections.Counter(s)[' ']+1
s="Hello, my name is John"
print(Solution().countSegments(s))
