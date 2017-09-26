from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a=[]
        for i in range(1,len(nums)+1):
            a+=list(combinations(nums,i))
        return list(map(list,a))
        

if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().subsets(nums))
