# Uses python3
import sys

def knapsack(W, wt, val, n):
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

if __name__ == '__main__':
    W, n = list(map(int, input().split()))
    wt = list(map(int, input().split()))
    val_per_weight = 1
    val = [val_per_weight*x for x in wt]
    print(knapsack(W, wt, val, n))
