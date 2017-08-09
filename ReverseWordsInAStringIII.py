class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])[::-1]

a=Solution()
s="Let's take LeetCode contest"
b=a.reverseWords(s)
print(b)
