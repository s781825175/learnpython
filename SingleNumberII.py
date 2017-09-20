class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1,len(nums)-1):
            if nums[i]==nums[i-1] or nums[i]==nums[i+1]:
                continue
            else:
                return nums[i]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
