from itertools import combinations
class Solution:
    def delele(self, a):
        for i in range(len(a)):
            b=a[0]
            a.pop(0)
            if b not in a:
                a.append(b)
        return a

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a=[]
        c=[]
        for i in range(1,len(nums)+1):
            b=list(map(list,list(combinations(nums,i))))
            a.append(b)
        for i in a:
            Solution().delele(i)
        for i in a:
            for j in i:
                c.append(j)
        return c

if __name__ == '__main__':
    nums=[1,2,2]
    print(Solution().subsetsWithDup(nums))
