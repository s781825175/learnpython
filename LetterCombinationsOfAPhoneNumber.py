from itertools import product
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        a=[["2","abc"]
        ,["3","def"]
        ,["4","ghi"]
        ,["5","jkl"]
        ,["6","mno"]
        ,["7","pqrs"]
        ,["8","tuv"]
        ,["9","wxyz"]]
        b=[]
        digits=list(digits)
        for i in digits:
            for j in a:
                if i == j[0]:
                    b.append(j[1])
        return list(product(*b))



if __name__ == '__main__':
    digits="234"
    print(Solution().letterCombinations(digits))
