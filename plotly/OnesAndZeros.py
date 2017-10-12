import collections
from itertools import combinations
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        a=''
        for i in list(strs):
            a+=i
        tot=collections.Counter(a)
        tar=tot-collections.Counter({'1': n, '0': m})
        ne=[]
        for i in strs:
            x=collections.Counter(i)
            ne.append(x) 
        a=ne[0]
        for i in range(len(ne)):
            if i==len(ne)-1:
                break
            a+=ne[i+1]
        for i in range(1,len(strs)+1):
            com=list(combinations(strs,i))
            for j in com:
                st=''
                for k in list(j):
                    st+=k
                    if collections.Counter(st)==tar:
                        return len(strs)-i


if __name__ == '__main__':
    strs = {"10", "0001", "111001", "1", "0"}
    m=5
    n=3
    print(Solution().findMaxForm(strs,m,n))
