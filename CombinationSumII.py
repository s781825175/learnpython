class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(lis,target):
            x=0
            a,d=[],[]
            for i in lis:
                x+=i
                if x > target:
                    x-=i
                elif x == target:
                    b=[]
                    a.append(i)
                    for j in a:
                        b.append(j)
                    x-=i
                    a.pop()
                    d.append(b)
                else:
                    a.append(i)
            return d
        candidates.sort(reverse=True)
        c=[]
        for i in range(len(candidates)):
            if bool(dfs(candidates[i:],target))==1:
                c.append(dfs(candidates[i:],target))
        c=[y for x in c for y in x]
        for i in range(len(c)-1,0,-1):
            if c[i] in c[:i]:
                c.pop(i)
        return c
            

        



if __name__ == '__main__':
    candidates=[10, 1, 2, 7, 6, 1, 5]
    target=8
    print(Solution().combinationSum2(candidates,target))
