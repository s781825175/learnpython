class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
            


nums=[2,7,11,16]
target=23
print(Solution().twoSum(nums, target))
