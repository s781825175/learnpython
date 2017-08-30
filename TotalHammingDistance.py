import collections
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        for i in range(len(nums)):
            for j in nums[i:]:
                a+=collections.Counter(str(bin(nums[i]^j)))['1']
        return a

if __name__ == '__main__':
    nums=[4,14,2]
    print(Solution().totalHammingDistance(nums))
