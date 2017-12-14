class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        m=[]
        for i in range(len(A)):
            a,b = 0,0
            for j in range(0-i,0-i+4):
                a += A[j] * b
                b += 1
            b = 0
            m.append(a)
        return max(m)

if __name__ == '__main__':
    A = [4, 3, 2, 6]
    print(Solution().maxRotateFunction(A))
