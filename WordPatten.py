class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        a=str.split()
        return bool(list(map(pattern.find, pattern))==list(map(a.index, a)))

pattern="abba"
str="dog cat cat dog"
print(Solution().wordPattern(pattern,str))
