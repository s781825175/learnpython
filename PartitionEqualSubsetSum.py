class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2 == 1:
            return False
        a = sum(nums)/2
        cur = {0}
        for i in nums:
            cur |= {i + x for x in cur}
            print(cur)
            if a in cur:
                return True


if __name__ == '__main__':
    nums=[1,5,5,11]
    print(Solution().canPartition(nums))
