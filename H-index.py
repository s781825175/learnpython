class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations=sorted(citations)[::-1]
        for i in range(1,len(citations)+1):
            if i > citations[i-1]:
                print(i,citations[i-1])
                return i-1

if __name__ == '__main__':
    citations=[3, 0, 6, 1, 5,4,4]
    print(Solution().hIndex(citations))