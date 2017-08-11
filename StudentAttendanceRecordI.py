import collections
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=collections.Counter(s)
        for i in range(len(s)-2):
            if list(s)[i]==list(s)[i+1]=='L' and list(s)[i]==list(s)[i+2]:
                return bool(0)
        return bool(a['A']<2)

s="PPALLL"
b=Solution().checkRecord(s)
print(b)
