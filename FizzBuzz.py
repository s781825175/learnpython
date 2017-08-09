class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [(i%3==0)*"Fizz" + (i%5==0)*"Buzz" or str(i) for i in range(1, n+1)]
a=Solution()
n=15
l=a.fizzBuzz(n)
print(l)
