class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a=nums[int(len(nums)/2)]
        return sum(abs(i-a) for i in nums)


if __name__ == '__main__':
    nums=[1,5,10,3]
    print(Solution().minMoves2(nums))
