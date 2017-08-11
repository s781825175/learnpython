import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

a=Solution()
ransomNote="aa"
magazine="aab"
b=a.canConstruct(ransomNote, magazine)
print(b)
