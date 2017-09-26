from itertools import product
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        a=time.replace(':','')
        b=list(product(a, repeat=4))
        nt=[]
        for i in b:
            c=int(''.join(i))
            if int(str(c)[:2])>24 or int(str(c)[2:])>60 or c<=int(a):
                continue
            nt.append(c)
        if len(nt)>0:
            return str(min(nt))[:2]+':'+str(min(nt))[2:]
        if len(nt)==0: 
            if '0' in a:
                return '00:00'
            elif '1' in a:
                return '11:11'
            else:
                return '22:22'

        

if __name__ == '__main__':
    time="23:33"
    print(Solution().nextClosestTime(time))
