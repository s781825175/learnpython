class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x=list(str(x))
        x=x[::-1]
        while x[0]=='0':
            x.pop(0)
        return ''.join(x)


if __name__ == '__main__':
    x=1241153128000
    print(Solution().reverse(x))

