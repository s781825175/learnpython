class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b=0
        for i in range(len(prices)-1,-1,-1):
            for j in range(len(prices)-1,-1,-1):
                if j>=i:
                    continue
                b=max(prices[i]-prices[j],b)
        return b

prices=[7, 1, 5, 3, 6, 4]
a=Solution().maxProfit(prices)
print(a)

