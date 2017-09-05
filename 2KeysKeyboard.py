class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        f=1
        for i in range(int(n**0.5),0,-1):
            print(i)
            if n%i == 0:
                f=i
                print(f)
                break
        if f == 1:
            return n
        return int(self.minSteps(f) + self.minSteps(n/f))



if __name__ == '__main__':
    n=100
    print(Solution().minSteps(n))
