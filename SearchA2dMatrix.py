class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        a=[]
        for i in matrix:
            a.append(i[0])
        if target < a[0]:
            return False
        if target > a[-1]:
            if taret in matrix[-1]:
                return True
        for i in range(len(a)):
            if target > a[i] and target <= a[i+1]:
                if target in matrix[i]:
                    return True
        return False

if __name__ == '__main__':
    matrix=[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
    target=3
    print(Solution().searchMatrix(matrix,target))
