import collections
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b=0,0
        num=[]
        for i in nums:
            if i == 0 or i == 1:
                num.append(i)
        for i in range(len(num),0,-1):
            for j in range(i):
                if collections.Counter(num[j:i])[0] == collections.Counter(num[j:i])[1]:
                    a=len(num[j:i])
                if a>b:
                    b=a
        return b




if __name__ == '__main__':
    nums=[0,1,0,1,0]
    print(Solution().findMaxLength(nums))
