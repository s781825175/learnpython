from itertools import combinations
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        nums=list(map(str,nums))
        num=''.join(nums)
        a=list(combinations(num, 3))
        b=[]
        a=list(map(list,a))
        for i in a:
            if int(i[0])+int(i[1])>int(i[2]):
                b.append(i)
        return len(b)

if __name__ == '__main__':
    nums=[2,2,2,3,4]
    print(Solution().triangleNumber(nums))
