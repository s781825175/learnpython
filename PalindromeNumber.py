class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0 or (x!=0 and x%10==0)): return false
        rev = 0
        while x>rev:
    	    rev = rev*10 + x%10
    	    x = x//10
        return bool(x==rev or x==rev/10)

x=1331
print(Solution().isPalindrome(x))

