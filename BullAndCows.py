class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A=0
        a=list(secret)
        b=list(guess)
        for i in range(len(guess)):
            if a[i]==b[i]:
                A+=1
        B=sum(min(secret.count(x),guess.count(x)) for x in '0123456789')
        return '%dA%dB' % (A,B-A)

if __name__ == '__main__':
    secret = "1807"
    guess = "7810"
    print(Solution().getHint(secret,guess))
