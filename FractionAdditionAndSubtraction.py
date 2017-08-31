import re,math
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        ints = map(int, re.findall('[+-]?\d+', expression))
        A, B = 0, 1
        for a in ints:
            b = next(ints)
            A = A * b + a * B
            B *= b
            g = math.gcd(A, B)
            A //= g
            B //= g
        return '%d/%d' % (A, B)        

if __name__ == '__main__':
    expression="1/3-1/2"
    print(Solution().fractionAddition(expression))
