class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        while nums[a]==nums[a+1]:
            a+=2
        return nums[a]
        
            

if __name__ == '__main__':
    nums=[1,1,3,3,7,4,4,8,8]
    print(Solution().singleNonDuplicate(nums))
