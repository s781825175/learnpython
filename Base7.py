class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        return (num//7)*10+num%7

num=777
print(Solution().convertToBase7(num))
