class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        


if __name__ == '__main__':
    nums=[1,2,3,1]
    print(Solution().findPeakElement(nums))

