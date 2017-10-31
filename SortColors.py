class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red=[]
        white=[]
        blue=[]
        for i in nums:
            if i == 0:
                red.append(i)
            elif i == 1:
                white.append(i)
            else:
                blue.append(i)
        total=red+white+blue
        return total

        

if __name__ == '__main__':
    nums=[2,0,1,0,2,0,1,1,2,0,0,1,2,1]
    print(Solution().sortColors(nums))
