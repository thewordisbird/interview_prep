# Matrix-chain Multiplication

# Given a chain (A1, A2, ... , An) of n matricies where for i = 1, 2, ..., n, matrix Ai has dimension pi-1 X pi,
# fully parenthesize the product A1A2...An in a way that minimizes the number of scalar multiplications.

def matrix_chain_order(p):
    # Initialize dp table
    dp = [[[0,0] for _ in range(len(p))] for _ in range(len(p))]

    for l in range(2, len(p)+1):
        for i in range(len(p)-l+1):
            j = i + l -1
            #print(i, j)
            dp[i][j][0] = float('inf')

            for k in range(i , j):
                
                q = dp[i][k][0] + dp[k+1][j][0] + cost(p, i, k, j)
                #print(l, i, j, k, cost(p, i, k, j), q)
                if q < dp[i][j][0]:
                    dp[i][j] = [q, k]
    return dp

def cost(p, i, k, j):
    return p[i][0] * p[k][1] * p[j][1]

def print_optimal_parens(dp, i, j):
    str = ''
    if i == j:
        return f' A{i} '
    else:
        str = str + "(" + \
        print_optimal_parens(dp, i, dp[i][j][1]) + \
        print_optimal_parens(dp, dp[i][j][1] + 1, j) + \
        ")"
    return str


if __name__ == "__main__":
    p = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]

    result = matrix_chain_order(p)

    print(print_optimal_parens(result, 0,5))
