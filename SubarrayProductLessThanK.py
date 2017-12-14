class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        m = 0
        for i in range(1,len(nums)+1):
            for j in range(i):
                x=1
                for i in nums[j:j+i]:
                    x*=i
                if x < k:
                    m += 1
        return m
        '''

        status = (1, 0) # (product of elements in window, left window)
        result = 0
        for i, num in enumerate(nums):
            product, left = status
            product *= num
            print(product,left)
            while product >= k and left < i+1:
                product /= nums[left]
                left += 1
            status = (product, left)
            result += i - left + 1  
            print(status,result)        
        return result

if __name__ == '__main__':
    nums = [10, 5, 2, 6]
    k = 100
    print(Solution().numSubarrayProductLessThanK(nums,k))
