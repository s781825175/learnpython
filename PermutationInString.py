class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        a=list(s1)[::-1]
        b=''
        for i in a:
            b+=i
        return (b in s2)


if __name__ == '__main__':
    s1='ab'
    s2='eidbaooo'
    print(Solution().checkInclusion(s1,s2))
