class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=list(range(2,n)) 
        c=[2]
        for i in a:
            b=0
            for j in a[:i-3]:
                if i % j == 0 :
                    b=1
                    break
            if b==0:
                c.append(i)
        return len(c)

if __name__ == '__main__':
    n=100
    print(Solution().countPrimes(n))
