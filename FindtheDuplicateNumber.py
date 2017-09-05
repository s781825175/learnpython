class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a=None
        for i in nums:
            if i==a:
                return i
            a=i

if __name__ == '__main__':
    nums=[1,2,3,2,2,6,5,4,7]
    print(Solution().findDuplicate(nums))
            
