#回文字符串
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[1] * 2 for _ in range(n)]
        for j in range(1, len(s)):
            for i in reversed(range(0, j)):
                if s[i] == s[j]:
                    dp[i][j%2] = 2 + dp[i + 1][(j - 1)%2] if i + 1 <= j - 1 else 2
                else:
                    dp[i][j%2] = max(dp[i + 1][j%2], dp[i][(j - 1)%2])
        return dp[0][(n-1)%2]

if __name__ == '__main__':
    s='abcdefghgggccfedcba'
    print(Solution().longestPalindromeSubseq(s))
