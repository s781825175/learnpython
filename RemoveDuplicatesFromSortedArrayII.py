class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        a=[]
        for i in range(1,len(nums)-1):
            if nums[i]==nums[i-1] and nums[i]==nums[i+1]:
                a.append(i)
        a=a[::-1]
        for i in a:
            nums.pop(i)
        return len(nums)

if __name__ == '__main__':
    nums=[1,1,1,1,1,1,1,1,2,2,2,2,3]
    print(Solution().removeDuplicates(nums))
