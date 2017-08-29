class Solution(object):
    def findPoisonedDuration(self, a, b):
        """
        :type a: List[int]
        :type b: int
        :rtype: int
        """
        c=[]
        for i in a:
            for j in range(i,i+b):
                c.append(j)
        return len(set(c))

if __name__ == '__main__':
    a,b=[1,2], 2
    print(Solution().findPoisonedDuration(a,b))

