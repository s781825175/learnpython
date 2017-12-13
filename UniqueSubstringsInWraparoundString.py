class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        s='abcdefghijklmnopqrstuvwxyz'*10
        a=0
        for i in range(len(p)):
            for j in range(len(p)-i):
                if s[j:j+i] in s:
                    a+=1
        return a

if __name__ == '__main__':
    p='zab'
    print(Solution().findSubstringInWraproundString(p))
