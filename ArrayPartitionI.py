#Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.Example 1:Input: [1,4,3,2]Output: 4Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])

if __name__ == '__main__':
    nums=[1,4,3,2,8,5,9,6]
    print(Solution().arrayPairSum(nums))
