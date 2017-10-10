class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-k]

if __name__ == '__main__':
    nums=[3,2,1,5,6,4]
    k=2
    print(Solution().findKthLargest(nums,k))
