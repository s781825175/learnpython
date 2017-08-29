class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=list(range(len(nums)))
        c=[]
        for i in nums:
            a,b=[],[]
            a.append(i)
            while len(a)==len(set(a)):
                b.append(num[a[-1]])
                print(b)
                a.append(nums[b[-1]])
                print(a)
            c.append(len(set(a)))
        c.sort()
        print(c)
        return c[-1]

if __name__ == '__main__':
    nums=[5,4,0,3,1,6,2]
    print(Solution().arrayNesting(nums))

