class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
a=Solution()     
s="hello"
s=a.reverseString(s)
print(s)
