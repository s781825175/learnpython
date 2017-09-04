import collections
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=['six','zero','eight','four','two','seven','five','three','one','nine']
        g=['6','0','8','4','2','7','5','3','1','9']
        d=['x','z','g','u','w']
        c=[]
        f=''
        h=''
        b=collections.Counter(s)
        for i in d:
            c.append(b[i])
        c.append(b['s']-c[0])
        c.append(b['v']-c[5])
        c.append(b['h']-c[2])
        c.append(b['o']-c[4]-c[1]-c[3])
        c.append(b['i']-c[2]-c[6]-c[0])
        for j in range(10):
            f+=a[j]*c[j]
            h+=g[j]*c[j]
        if sorted(list(f))==sorted(s):
            return h
        else:   return False



if __name__ == '__main__':
    s="fviefuo"
    print(Solution().originalDigits(s))
