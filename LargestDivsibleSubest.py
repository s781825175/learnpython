class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=sorted(nums)[::-1]
        tot=[]
        for i in range(len(nums)):
            a=[]
            for j in nums[i:]:
                if j in nums[i:]:
                    a.append(j)
            tot.append([a,len(a)])
        a=sorted(tot, key=lambda x:x[1])
        return a[-1][0]

if __name__ == '__main__':
    nums = [1,2,4,8]
    print(Solution().largestDivisibleSubset(nums))
