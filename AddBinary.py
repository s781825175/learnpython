class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return ''.join(list(str(bin(int(a,base=2)+int(b,base=2))))[2:])
a='11'
b='1'
print(Solution().addBinary(a,b))
