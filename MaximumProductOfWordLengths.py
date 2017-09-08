from itertools import combinations
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        b=list(combinations(words,2))
        d=[]
        for i in b:
            c=i[0]+i[1]
            if len(c)==len(set(c)):
                d.append(len(i[0])*len(i[1]))
        return max(d)



if __name__ == '__main__':
    words=["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    print(Solution().maxProduct(words))
