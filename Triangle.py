class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        return sum(min(i) for i in triangle)

if __name__ == '__main__':
    triangle=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print(Solution().minimumTotal(triangle))
