class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=0
        for i in range(1,len(nums)-1):
            if nums[i]<nums[i-1] and nums[i]>nums[i+1]:
                return False
            if nums[i]<nums[i-1] or nums[i]>nums[i+1]:
                a+=1
                if a>1:
                    return False
        return True

if __name__ == '__main__':
    nums=[4,2,1]
    print(Solution().checkPossibility(nums))
