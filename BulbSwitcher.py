import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))


if __name__ == '__main__':
    n=35
    print(Solution().bulbSwitch(n))
        
