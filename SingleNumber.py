class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(set(nums)))*2 - sum(nums)
a=Solution()
nums=[1,1,2,3,2,6,6]
b=a.singleNumber(nums)
print(b)
