class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        b=0
        s=sorted(intervals,key=lambda i: i[1])
        for i in range(len(s)):
            if i==len(s)-1:
                break
            if s[i+1][0] >= s[i][1]:
                a=s[i][1]
            else:
                b+=1
        return b
        

if __name__ == '__main__':
    intervals=[ [1,2], [2,3], [3,4], [1,3] , [1,2], [2,3] ]
    print(Solution().eraseOverlapIntervals(intervals))
