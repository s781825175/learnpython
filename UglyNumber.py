class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        a=[]
        while num!=1:
            for i in range(2,num):
                if num%i==0:
                    a.append(i)
                    num/=i
        return bool(not a[-1]>5)
num=14
print(Solution().isUgly(num))
