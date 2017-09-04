from itertools import combinations
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        a=combinations(words,2)
        b=[]
        c=0
        d=[]
        for i in a:
            for j in list(i[0]):
                c=1
                if i[1].find(j)>-1:
                    c=0
                    break
            if c==1:
                b.append([i[0],i[1]])
        for k in b:
            d.append(len(k[0])*len(k[1]))
        d.sort()
        return d[-1]


if __name__ == '__main__':
    words=["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    print(Solution().maxProduct(words))
