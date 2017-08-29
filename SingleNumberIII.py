class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        b=[]
        nums.sort()
        a=1
        while a<len(nums)-1:
            if nums[a]==nums[a+1] or nums[a]==nums[a-1]:
                a+=1
            else:   
                b.append(nums[a])
                a+=1
        if nums[-1]!=nums[-2]:
            b.append(nums[-1])
        return b

if __name__ == '__main__':
    nums = [1, 2, 1, 3, 2, 5]
    print(Solution().singleNumber(nums))

