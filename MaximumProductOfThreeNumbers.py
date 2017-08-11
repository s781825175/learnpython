import itertools
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        del nums[3:-3]
        return max(a*b*c for a,b,c in itertools.combinations(nums, 3))

nums=[2,4,5,3]
a=Solution().maximumProduct(nums)
print(a)
