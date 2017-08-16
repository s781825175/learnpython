class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        for i in range(len(nums)-k-1):
            a=max(sum(nums[i:i+k]),sum(nums[i+1:i+1+k]))/k 
        return a
nums=[1,12,-5,-6,50,3]
k = 4
print(Solution().findMaxAverage(nums,k))
