class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        a=timePoints
        for i in range(len(a)):
            a[i]=a[i].split(':')
        b=min(abs(int(a[1][1])-(int(a[0][1]))),abs(int(a[1][1])+60-int(a[0][1])))
        if a[1][0]<a[0][0]: c=24+int(a[1][0])-int(a[0][0])
        else:   c=int(a[1][0])-int(a[0][0])
        if a[1][1]<a[0][1]:
            c-=1
        return c*60+b

if __name__ == '__main__':
    timePoints=["02:59","00:00"]
    print(Solution().findMinDifference(timePoints))
