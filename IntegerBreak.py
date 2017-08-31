from functools import reduce
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <4:
            return n-1
        a=[3]*(int(n/3))
        if n%3==2:
                a.append(2)
        elif n%3==1:
            a[0]=(4)
        return reduce(lambda x,y:   x*y,a)


if __name__ == '__main__':
    n=4
    print(Solution().integerBreak(n))

