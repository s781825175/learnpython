import collections
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=collections.Counter(nums)
        nums.sort()
        b=0
        for i in range(int(nums[-1])):
            b=max(a[i]+a[i+1], b)
        return b
        
nums=[1,3,2,2,5,2,3,7]
print(Solution().findLHS(nums))
