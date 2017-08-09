class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candy=set(candies)
        if len(candy)>=len(candies)/2:
            s=len(candies)/2
        else:
            s=len(candy)
        return int(s)
#oneline:return min(len(candies) / 2,len(set(candies)))

a=Solution()
candies = [1,1,2,3]
s=a.distributeCandies(candies)
print(s)

