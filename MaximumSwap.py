class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        places = [10**i for i in range(len(str(num)))]
        return max(num + num/p%10*(q-p) + num/q%10*(p-q)
            for p in places for q in places)


if __name__ == '__main__':
    num=2736
    print(Solution().maximumSwap(num))
