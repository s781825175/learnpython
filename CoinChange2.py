def dfs(amount,coins):
    dp = [0] * (amount+1)
    dp[0] = 1
    for i in coins:
        for j in range(1, amount+1):
            print(i,j,dp)
            if j >= i:
                dp[j] += dp[j-i]
    return dp[-1]


if __name__ == '__main__':
    amount = 5
    coins = [1,2,5]
    print(dfs(amount,coins))

