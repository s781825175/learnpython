class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k==0:
            return len(nums)-len(set(nums))
        else:
            return len(set(nums)&set(n+k for n in nums))

nums=[3, 1, 4, 1, 5]
k=2
print(Solution().findPairs(nums, k))
