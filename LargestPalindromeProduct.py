class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[]
        for i in range(10**(n-1),10**n):
            for j in range(10**(n-1),10**n):
                k=i*j
                if list(str(k))==list(str(k))[::-1]:
                    a.append(k)
        a.sort()
        return a[-1]%1337
if __name__ == '__main__':
    n=2
    print(Solution().largestPalindrome(n))
