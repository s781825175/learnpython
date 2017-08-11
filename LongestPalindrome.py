import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        n=list(collections.Counter(s).values())
        for i in range(len(n)):
            if n[i]&1==0:
                l+=int(n[i])
            else:
                l+=(int(n[i])-1)
        return l+1

s="abccccdd"
a=Solution().longestPalindrome(s)
print(a)
