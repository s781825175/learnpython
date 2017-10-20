class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b=None,None
        c,tot=1,[]
        for i in nums:
            a=i
            d=1
            for j in range(c,len(nums)):
                if nums[j]>a:
                    a,b=nums[j],a
                    d+=1
                if type(b)==int:    
                    if nums[j]<a and nums[j]>b:
                        a=nums[j]
            tot.append(d)
            c+=1 
        return (max(tot))



        

if __name__ == '__main__':
    nums=[10, 9, 2, 5, 3, 7, 101, 18,19]
    print(Solution().lengthOfLIS(nums))
