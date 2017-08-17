class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        a=[1]
        for i in range(2,int(num/2)):
            if num%i==0:
                a.append(i)
                a.append(num//i)
        return (sum(set(a))==num)
num=120
print(Solution().checkPerfectNumber(num))
