from operator import itemgetter
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        s=list(s)
        b=[]
        c=None
        for j in d:
            j=list(j)
            b.append(c)
            c=0
            for k in j:
                a=0
                for i in range(len(s)):
                    if k==s[a:][i-a]:
                        a=i
                        c+=1
                        break
        b.append(c)
        b.pop(0)
        zi=list(zip(b,d))
        a=[]
        for i in range(len(zi)):
            if zi[i][0]==len(zi[i][1]):
                a.append(zi[i])
        return max(a,key=itemgetter(0))[1]
        
if __name__ == '__main__':
    d = ["ale","apple","monkey","plea"]
    s = "abpcplea"
    print(Solution().findLongestWord(s,d))

