from itertools import combinations
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(map(list,list(combinations(range(1,n+1),k))))

if __name__ == '__main__':
    n,k=4,2
    print(Solution().combine(n,k))
