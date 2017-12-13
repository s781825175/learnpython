class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[]
        for i in range(2,2000):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                a.append(i)
            if len(a) + n == i:
                return i


if __name__ == '__main__':
    n=10
    print(Solution().nthUglyNumber(n))
