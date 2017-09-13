class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a,b=sorted(nums),[1]+[0]*(target)
        for i in range(target+1):
            for j in a:
                if j>i: break
                if j==i: b[i]+=1
                if j<i: b[i]+=b[i-j]
                print(i,j)
        return b[target]

if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    print(Solution().combinationSum4(nums,target))

