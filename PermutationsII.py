from itertools import permutations
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a = list(permutations(nums,len(nums)))
        b = []
        for _ in range(len(nums)):
            n = a[0]
            a.pop(0)
            if n not in nums:
                b.append(n)
        return b



if __name__ == '__main__':
    nums=[1,1,2]
    print(Solution().permuteUnique(nums))
