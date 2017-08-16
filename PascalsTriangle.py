class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        num = [[1], [1, 1]]
        if numRows == 1:
            return num[0]
        elif numRows == 2:
            return num
        elif numRows == 0:
            return []
        row = []
        for i in range(2, numRows):
            for j in range(i - 1):
                row.append(sum(num[-1][j:j + 2]))
            num.append([1] + row + [1])
            row = []

        return num
numRows=5
print(Solution().generate(numRows))
