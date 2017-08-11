class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(1,len(numbers)+1):
            for j in range(1,len(numbers)+1):
                if numbers[i-1]+numbers[j-1]==target:
                    return i,j


a=Solution()
numbers=[2,7,11,16]
target=9
b=a.twoSum(numbers, target)
print(b)
