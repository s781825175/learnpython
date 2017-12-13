class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        left,top = max(A,E),max(B,F)
        right,bot = max(min(C,G),left),max(min(D,H),top)
        return (C-A)*(D-B) - (right-left)*(bot-top) + (G-E)*(H-F)
        


if __name__ == '__main__':
    A,B,C,D,E,F,G,H = -3,0,3,4,0,-1,9,2
    print(Solution().computeArea(A,B,C,D,E,F,G,H))


