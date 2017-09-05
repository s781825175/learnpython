import itertools
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(itertools.permutations(nums))

if __name__ == '__main__':
    nums=[1,2,3]
    print(Solution().permute(nums))
