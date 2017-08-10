class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(map(len, ''.join(map(str, nums)).split('0')))

a=Solution()
nums=[1,1,0,1,1,1,0,1]
b=a.findMaxConsecutiveOnes(nums)
print(b)
