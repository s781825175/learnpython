#hammingDistancec
class Solution(object):
    def hammingDistance(self, x, y):
        a=list(str(bin(x^y)))
        n=a.count('1') 
        return n
m=Solution()
x=int(input())
y=int(input())
n=m.hammingDistance(x, y)
print(n)
