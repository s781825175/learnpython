from itertools import combinations
import math
class Solution(object):
    def validSquare(self, a, b, c, d):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        t=[a,b,c,d]
        e=list(combinations(t,2))
        print(e)
        f=[]
        for i in e:
            f.append(math.sqrt((i[0][0]-i[1][0])**2+(i[0][1]-i[1][1])**2))
        print(f)
        if sorted(f)[4] != sorted(f)[-1]:
            return False
        if math.sqrt(min(f)**2+min(f)**2) != max(f):
            return False
        if sorted(f)[0]==sorted(f)[1]==sorted(f)[2]==sorted(f)[3]:
            return True


if __name__ == '__main__':
    a = [0,0]
    b = [1,1]
    c = [1,0]
    d = [0,1]
    print(Solution().validSquare(a,b,c,d))
