class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        a=[chr(x) for x in range(ord('A'),ord('Z')+1)]
        s=[]
        while n > 0:
            s.append(a[(n-1)%26])
            n=(n-1)//26
        s=s[::-1]
        s=''.join(s)
        print(s)

if __name__ == '__main__':
    n=26
    Solution().convertToTitle(n)

