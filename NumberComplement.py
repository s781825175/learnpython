#输出补码
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i=0
        while 2**i<num:
            i+=1
        return (2**i-1)^num
a=Solution()
num=int(input())
b=a.findComplement(num)
print(b)
