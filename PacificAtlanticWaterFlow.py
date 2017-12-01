class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def lefpac(matrix,ij,ori,lis):
            if lis[0] == 0 or lis[1] == 0:
                return ij
            if matrix[lis[0]][lis[1]] >= matrix[lis[0]][lis[1]-1]:
                ori = [lis[0],lis[1]]
                lis = [lis[0],lis[1]-1]
                return lefpac(matrix,ij,ori,lis)
            else:
                return uppac(matrix,ij,ori,lis)

        def uppac(matrix,ij,ori,lis):
            if lis[0] == 0 or lis[1] == 0:
                return ij
            if matrix[lis[0]][lis[1]] >= matrix[lis[0]-1][lis[1]]:
                ori = [lis[0],lis[1]]
                lis = [lis[0]-1,lis[1]]
                return uppac(matrix,ij,ori,lis)
            else:
                if matrix[lis[0]][lis[1]] < matrix[lis[0]][lis[1]-1]:
                    return 0
                else:
                    lis = ori 
                    return uppac(matrix,ij,ori,lis)

            return 0
        
        def lefatl(matrix,ij,ori,lis):
            if lis[0] == 4 or lis[1] == 4:
                return ij
            if matrix[lis[0]][lis[1]] >= matrix[lis[0]][lis[1]+1]:
                ori = [lis[0],lis[1]]
                lis = [lis[0],lis[1]+1]
                return lefatl(matrix,ij,ori,lis)
            else:
                return upatl(matrix,ij,ori,lis)

        def upatl(matrix,ij,ori,lis):
            if lis[0] == 4 or lis[1] == 4:
                return ij
            if matrix[lis[0]][lis[1]] >= matrix[lis[0]+1][lis[1]]:
                ori = [lis[0],lis[1]]
                lis = [lis[0]+1,lis[1]]
                return upatl(matrix,ij,ori,lis)
            else:
                if matrix[lis[0]][lis[1]] < matrix[lis[0]][lis[1]+1]:
                    return 0
                else:
                    lis = ori 
                    return upatl(matrix,ij,ori,lis)
            return 0
        pac=[]
        atl=[]
        tot=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ij=[i,j]
                ori=[i,j]
                lis=[i,j]
                pac.append(lefpac(matrix,ij,ori,lis))
                atl.append(lefatl(matrix,ij,ori,lis))
        for i in range(len(pac)-1,-1,-1):
            if pac[i]==0:
                pac.pop(i)
        for i in range(len(atl)-1,-1,-1):
            if atl[i]==0:
                atl.pop(i)
        for i in pac:
            if i in atl:
                tot.append(i)
        return tot
        



if __name__ == '__main__':
    matrix=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(Solution().pacificAtlantic(matrix))
