class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a,b=0,0
        if nums[0]==0:
            a=1
        for i in range(len(nums)):
            if a==nums[i]:
                nums[i]=(nums[-1]+1)
                b+=1
            else:
                a=nums[i]
        nums.sort()
        for _ in range(b):
            nums.pop()
            c=nums
        return len(c)

nums=[1,3,4,1,2,5,21,1,2,3]
print(Solution().removeDuplicates(nums))
