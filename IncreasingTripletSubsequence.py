class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-3):
            a=nums[i:i+3]
            if a[0]<a[1] and a[1]<a[2]:
                return True
        return False

if __name__ == '__main__':
    nums=[5, 4, 3, 2, 1]
    print(Solution().increasingTriplet(nums))
