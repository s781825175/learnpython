class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ret, shoot = 0, float('inf')
        for s, e in sorted(points, reverse=True):
            if shoot > e:
                shoot = s
                ret += 1
        return ret

if __name__ == '__main__':
    points=[[10,16], [2,8], [1,6], [7,12]]
    print(Solution().findMinArrowShots(points))
