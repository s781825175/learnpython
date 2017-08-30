import collections
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        a=[]
        for i in M:
            a.append(collections.Counter(i)[0])
        return 1+min(a)

if __name__ == '__main__':
    M=[[1,1,0],[1,1,0],[0,0,1]]
    print(Solution().findCircleNum(M))
