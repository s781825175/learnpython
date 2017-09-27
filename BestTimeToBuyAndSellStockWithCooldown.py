class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        free = 0
        have = cool = float('-inf')
        for p in prices:
            free, have, cool = max(free, cool), max(have, free - p), have + p
            print(free, have, cool)
        return max(free, cool)


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    print(Solution().maxProfit(prices))
