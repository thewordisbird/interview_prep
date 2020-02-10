def ball_drop_1(arr):
    # Topological order from top to bottom, left to right. Emulates how ball would fall. 
    # Need to take max of dp[n -1] to find answer

    dp = [[0 for j in range(len(arr[i]))] for i in range(len(arr))]
    dp[0][0] = arr[0][0]

    for i in range(1, len(arr)):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = arr[i][j] + dp[i-1][j]
            elif j == i:
                dp[i][j] = arr[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] =  arr[i][j] + max(dp[i-1][j], dp[i-1][j-1])

    return max(dp[len(arr) -1])
    
def ball_drop_2(arr):
    # Topological order from bottom to top, right to left. 
    # This will give the final answer as dp[0][0]

    # This is a more elegant solution since you don't need as many edge cases
    # and the answer doesn't require an extra function call.

    dp = [[0 for j in range(len(arr))] for i in range(len(arr))]

    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(arr[i]) - 1, -1, -1):
            if i == len(arr) - 1:
                dp[i][j] = arr[i][j]
            else:
                dp[i][j] = arr[i][j] + max(dp[i+1][j], dp[i+1][j+1]) 

    return dp[0][0]

def ball_drop_3(arr):
    # Top down suffix sub problem
    cache = {}
    i = 0
    j = 0
    return _ball_drop_3(arr, i, j, cache)

def _ball_drop_3(arr, i, j, cache):
    if i == len(arr):
        return 0
    
    if (i,j) in cache:
        return cache[i,j]

    result =  arr[i][j] + max(_ball_drop_3(arr, i+1, j, \
        cache), _ball_drop_3(arr, i+1, j+1, cache))
    
    cache[(i,j)] = result
    r
    eturn result


if __name__ == "__main__":
    arr = [
            [7],
            [3, 8],
            [8, 1, 0],
            [2, 7, 4, 4],
            [4, 5, 2, 6, 5]
        ]

    print(ball_drop_1(arr))
    print(ball_drop_2(arr))
    print(ball_drop_3(arr))


