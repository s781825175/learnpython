class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=a.split('+')
        aa,ab=a[0],a[-1].split('i')[0]
        b=b.split('+')
        ba,bb=b[0],b[-1].split('i')[0]
        [aa,ab,ba,bb]=map(int, [aa,ab,ba,bb])
        a,b,c=aa*ba,aa*bb+ab*ba,ab*bb*(-1)
        return str(a+c)+'+'+str(b)+'i'

if __name__ == '__main__':    
    a="1+-1i"
    b="1+-1i"
    print(Solution().complexNumberMultiply(a,b))
