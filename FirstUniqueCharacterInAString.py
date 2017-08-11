class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            for j in range(len(s)):
                if i==j:
                    continue
                if list(s)[i]==list(s)[j]:
                    break
                if j==len(s)-1:
                    return i
        return -1
a=Solution()
s="lel"
b=a.firstUniqChar(s)
print(b)
