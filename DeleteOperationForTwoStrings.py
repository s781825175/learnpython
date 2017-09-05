#处理2行字符串，寻找2个字符串顺相同字符的个数
def minDistance(a,b):
        m, n = len(a), len(b)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (a[i] == b[j]))
        print(dp)
        return m + n - 2 * dp[m][n]

if __name__ == '__main__':
    a="seaogfolnka"
    b="egamgaekat"
    print(minDistance(a,b))
