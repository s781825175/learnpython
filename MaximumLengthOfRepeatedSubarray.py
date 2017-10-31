class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        a=[]
        for i in range(len(B)):
            for j in range(i+1,len(B)+1):
                b=B[i:j]
                a.append(b)
        for i in range(len(A),0,-1):
            for j in range(len(A)-i+1):
                if A[j:j+i] in a:
                    return i


if __name__ == '__main__':
    A=[1,2,3,2,1]
    B=[3,2,1,4,7]
    print(Solution().findLength(A,B))
