#Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.Example 1:Input: [1,4,3,2]Output: 4Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)/2
        l=int(l)
        nums.sort()
        m=nums[:l]
        n=nums[l:(l+l)]
        sum=min(m)+min(n)
        return sum
a=Solution()
nums=[1,4,3,2,8,5,9,6]
sum=a.arrayPairSum(nums)
print(sum)
