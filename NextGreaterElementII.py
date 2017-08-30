class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(len(nums)):
            for j in nums[i:]:
                if i == len(nums)-1:
                    a.append(a[0])
                    break
                if j>nums[i]:
                    a.append(j)
                    break
            if len(a)==i:
                a.append(-1)
        return a

if __name__ == '__main__':
    nums=[1,2,3,1]
    print(Solution().nextGreaterElements(nums))
