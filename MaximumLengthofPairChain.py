class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x:x[1])
        a=[pairs[0]]
        for i in pairs:
            if i[0]>a[-1][1]:
                a.append(i)
        return len(a)

if __name__ == '__main__':
    pairs=[[1,2], [2,3], [3,4]]
    print(Solution().findLongestChain(pairs))

