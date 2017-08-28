class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        b=[]
        for i in nums:
            a=0
            for j in nums[::-1]:
                if i == j:
                    a+=1
            if a>1:
                b.append(i)
        return list(set(b))


if __name__ == '__main__':
    nums=[4,3,2,7,8,2,3,1]
    print(Solution().findDuplicates(nums))
