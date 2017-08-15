class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
            print(maxSum,curSum)

        return maxSum

nums=[-2,1,-300,4,-1,2,1,-100,4]
print(Solution().maxSubArray(nums))
           
