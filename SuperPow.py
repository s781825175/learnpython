class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        b=list(map(str,b))
        b=int(''.join(b))
        return pow(a,b,1337) 

if __name__ == '__main__':
    a=2
    b=[1,0]
    print(Solution().superPow(a,b))
