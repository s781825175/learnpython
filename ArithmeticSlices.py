class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a,b,c,l,n=0,None,None,1,0
        for i in range(len(A)-1):
            b,c=c,A[i]-A[i+1]
            if b==c:
                l+=1
            else:
                n+=sum(list(range(l)))
                l=1
        return n+sum(list(range(l)))

if __name__ == '__main__':
    A=[1,2,3,4,7,8,9,7]
    print(Solution().numberOfArithmeticSlices(A))
