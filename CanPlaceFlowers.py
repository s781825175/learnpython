class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        a=0
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i]==flowerbed[i-1] and flowerbed[i]==flowerbed[i+1] and flowerbed[i]==0:
                a+=1
                flowerbed[i]=1
                print(a)
        return (a>=1)
flowerbed = [1,0,0,0,1]
n = 1
print(Solution().canPlaceFlowers(flowerbed, n))
