#Uses python3

import sys

def lcs3(X, Y, Z):
    m, n, o  = len(X), len(Y), len(Z)
    dp = [[[0 for i in range(o+1)] for j in range(n+1)] for k in range(m+1)]
    # print(dp)

    for i in range(0, m+1):
        for j in range(0, n+1):
            for k in range(0, o+1):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 0
                elif X[i-1] == Y[j-1] and X[i-1] == Z[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(max(dp[i-1][j][k], dp[i][j-1][k]), dp[i][j][k-1])

    return dp[m][n][o]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    b = list(map(int, input().split()))
    l = int(input())
    c = list(map(int, input().split()))
    # a = ''.join(a.split())
    # b = ''.join(b.split())
    print(lcs3(a, b, c))
