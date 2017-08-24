import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=re.compile('\W')
        s=a.sub('',s)
        a=re.compile('\d')
        s=a.sub('',s)
        s=s.lower()
        return (s==s[::-1])


if __name__ == "__main__":
    s="A man, a pl1an, a canal: Panama"
    print(Solution().isPalindrome(s))

