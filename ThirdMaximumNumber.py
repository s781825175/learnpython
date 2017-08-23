class Solution(object):
    def thirdmax(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        nums.sort()
        nums=list(set(nums))
        if len(nums)<3:
            return nums[-1]
        else:
            return nums[-3]

nums=[2,2,3,1]
print(Solution().thirdmax(nums))
