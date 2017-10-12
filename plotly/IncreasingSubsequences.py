from itertools import combinations
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tar=[]
        for i in range(2,len(nums)+1):
            tar+=list(set(list(combinations(nums,i))))
        return list(map(list, tar))
        

if __name__ == '__main__':
    nums=[4,6,7,7]
    print(Solution().findSubsequences(nums))
