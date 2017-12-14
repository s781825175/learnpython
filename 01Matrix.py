class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        zero,el = [],[]
        out = [[] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero.append([i,j,0])
                else:
                    el.append([i,j])
        for i in el:
            dis = []
            for j in zero:
                dis.append(abs(i[0]-j[0])+abs(i[1]-j[1]))
            i.append(min(dis))
        tot = sorted(el+zero, key=lambda x:x[1])
        for i in tot:
            out[i[0]].append(i[2])
        return out

if __name__ == '__main__':
    matrix = [[0,0,0],[0,1,0],[1,1,1]]
    print(Solution().updateMatrix(matrix))
