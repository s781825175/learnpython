class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        for i in range(len(nums)):
            a=nums[i]
            b=i+1
            while a < k:
                b+=1
                if b >= len(nums)+1:
                    break
                a = sum(nums[i:b])
                print(a,b)
            if a == k:
                c+=1
        return c

if __name__ == '__main__':
    nums=[1,2,3,2]
    k=5
    print(Solution().subarraySum(nums,k))
