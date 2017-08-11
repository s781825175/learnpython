import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return bool(collections.Counter(s)==collections.Counter(t))
s="anagram"
t="nagaram"
a=Solution().isAnagram(s, t)
print(a)
