import collections
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        a=list(range(num+1))
        a=list(map(bin,a))
        a=list(map(str,a))
        b=[]
        for i in a:
            b.append(collections.Counter(i)['1'])
        return b

if __name__ == '__main__':
    num=5
    print(Solution().countBits(num))
