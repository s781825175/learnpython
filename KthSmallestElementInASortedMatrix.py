class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        a=[]
        for i in matrix:
            a+=i
        a.sort()
        return a[k-1]


if __name__ == '__main__':
    matrix = [[ 1,  5,  9],[10, 11, 13],[12, 14, 15]]
    k = 8
    print(Solution().kthSmallest(matrix, k))
