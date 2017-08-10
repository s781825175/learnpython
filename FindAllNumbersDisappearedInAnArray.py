class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set([i for i in range(1,len(nums)+1)])-set(nums))
a=Solution()
nums=[4,3,2,7,8,2,3,1]
b=a.findDisappearedNumbers(nums)
print(b)
