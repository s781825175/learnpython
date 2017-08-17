class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return bool([s.find(i) for i in s]==[t.find(h) for h in t])
s,t="egg","add"
print(Solution().isIsomorphic(s,t))
