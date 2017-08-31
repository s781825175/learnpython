import collections
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[1,2,2]
        b=2
        while len(a)<n+1:
            a += a[b] * [3 - a[-1]]
            b += 1
        print(a)
        return collections.Counter(list(a)[:n])[1]

if __name__ == '__main__':
    n=6
    print(Solution().magicalString(n))
