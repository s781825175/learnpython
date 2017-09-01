from itertools import combinations
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k > 9 or k < 1:  return False
        if sum(list(range(1,10))[-k:])<n:   return False
        test = combinations(list(range(1,10)),k)
        a=[]
        for i in test:
            if sum(i)==n:
                a.append(i)
        return a
            
        


if __name__ == '__main__':
    k,n=3,9
    print(Solution().combinationSum3(k,n))
