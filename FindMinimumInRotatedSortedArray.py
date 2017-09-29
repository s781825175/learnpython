class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return nums[i+1]
        return nums[0]


if __name__ == '__main__':
    nums=[0,1,2,4,5,6,7]
    print(Solution().findMin(nums))
