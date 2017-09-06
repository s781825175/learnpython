import itertools
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        num=list(map(str,nums))
        l=0
        for i in range(len(nums)+1):
            a='+'*i+'-'*(len(nums)-i)
            a=list(a)
            c=list(set(list(itertools.permutations(a))))
            for k in c:
                b=''
                for j in range(len(a)):
                    b=b+k[j]+num[j]
                if eval(b)==S:
                    l+=1
        return l


if __name__ == '__main__':
    nums=[1,1,1,1,1]
    S=3
    print(Solution().findTargetSumWays(nums,S))
