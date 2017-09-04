class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        a=list(set(word1+word2))
        print(a)


        

if __name__ == '__main__':
    word1,word2 = 'sea','eat'
    print(Solution().minDistance(word1,word2))
