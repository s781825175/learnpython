class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        a=list(range(1,1+n))
        for i in range(1,k):
            a[i:]=a[:i-1:-1]
        return a

if __name__ == '__main__':
    n,k=3,2
    print(Solution().constructArray(n,k))
