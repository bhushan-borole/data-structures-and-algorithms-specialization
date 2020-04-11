#Uses python3

import sys

def lcs2(X, Y):
    m, n  = len(X), len(Y)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(0,m+1):
        for j in range(0,n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    b = list(map(int, input().split()))
    # a = ''.join(a.split())
    # b = ''.join(b.split())
    print(lcs2(a, b))
