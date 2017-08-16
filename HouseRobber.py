class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b=0,0
        for i in nums:
            a,b=b,max(a+i,b)
        return b

nums=[1,5,2,34,67,34,21,3,2,23,5,2,3]
print(Solution().rob(nums))
