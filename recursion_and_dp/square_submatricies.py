def count_squares(matrix):

    # Initiate DP table
    dp = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

    # Count number of 1's in table
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 and j == 0:
                dp[i][j] = matrix[i][j]
            elif i == 0:
                dp[i][j] = matrix[i][j] + dp[i][j-1]
            elif j == 0:
                dp[i][j] = matrix[i][j] + dp[i-1][j]
            else:
                dp[i][j] = matrix[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

    # append count for number of compopsed squares
    composite_squares = 0
    print(min(len(matrix), len(matrix[0])))
    for k in range(2, min(len(matrix), len(matrix[0])) + 1):
        for i in range(len(matrix)-1, k-2, -1):
            for j in range(len(matrix[i])-1, k-2, -1):
                
                square_count = 0
                
                if i - k == -1 and j - k == -1:
                    square_count = dp[i][j]
                elif i - k == -1:
                    square_count = dp[i][j] - dp[i][j-k]
                elif j - k == -1:
                    square_count = dp[i][j] - dp[i-k][j]
                else:
                    square_count = dp[i][j] - dp[i-k][j] - dp[i][j-k] + dp[i-k][j-k]
                
                print(i,j,k, square_count)
                if square_count == k ** 2:
                    composite_squares += 1
                
    return dp[-1][-1] + composite_squares

if __name__ == "__main__":
    matrix = [
                [0,1,1,1],
                [1,0,1,1],
                [0,1,1,1]
            ]   

print(count_squares(matrix))