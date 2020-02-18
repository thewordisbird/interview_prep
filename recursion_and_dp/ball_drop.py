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

    return (dp, max(dp[len(arr) -1]))

def get_path_1(arr, dp):
    # Find j for max in last row of dp
    j_max_val = -float('inf')
    j_max_index = 0
    i_max_index = len(dp) - 1
    for j,v in enumerate(dp[i_max_index]):
        if v > j_max_val:
            j_max_val = v
            j_max_index = j
    
    
    path = []
    path.append(arr[i_max_index][j_max_index])
    i_index = i_max_index - 1
    j_index = j_max_index
    j_val = j_max_val - arr[i_max_index][j_max_index]
    while i_index >= 0:
        if dp[i_index][j_index] == j_val:
            path.append(arr[i_index][j_index])
            j_val = j_val - arr[i_index][j_index]
        else: # This ordering should prevent j_index out of bounds
            path.append(arr[i_index][j_index - 1])
            j_val = j_val - arr[i_index][j_index - 1]
            j_index -= 1
        i_index -=1

    return list(reversed(path))

    
def ball_drop_2(arr):
    # Topological order from bottom to top, right to left. 
    # This will give the final answer as dp[0][0]

    # This is a better solution since you don't need as many edge cases
    # and the answer doesn't require an extra max function call.

    dp = [[0 for j in range(len(arr))] for i in range(len(arr))]

    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(arr[i]) - 1, -1, -1):
            if i == len(arr) - 1:
                dp[i][j] = arr[i][j]
            else:
                dp[i][j] = arr[i][j] + max(dp[i+1][j], dp[i+1][j+1]) 

    return (dp, dp[0][0])

def get_path_2(arr, dp):
    i_index = j_index = 0
    path = [arr[i_index][j_index]]
    j_val = dp[i_index][j_index] - arr[i_index][j_index]
    i_index += 1
    while i_index < len(dp):
        if dp[i_index][j_index] == j_val:
            path.append(arr[i_index][j_index])
            j_val -= arr[i_index][j_index]
        else:
            path.append(arr[i_index][j_index + 1])
            j_val -= arr[i_index][j_index + 1]
            j_index += 1
        i_index += 1
    return path


def ball_drop_3(arr):
    # Top down suffix sub problem
    cache = {}
    child = {}
    i = 0
    j = 0
    max_score = _ball_drop_3(arr, i, j, cache, child)
    path = get_path_3(arr, child)
    return (path, max_score)

def _ball_drop_3(arr, i, j, cache, child):
    if i == len(arr):
        return 0
    
    if (i,j) in cache:
        return cache[i,j]

    else:
        left = _ball_drop_3(arr, i+1, j, cache, child)
        right = _ball_drop_3(arr, i+1, j+1, cache, child)
        if left > right:
            result =  arr[i][j] + left
            child[(i, j)] = (i+1, j)
        else:
            result =  arr[i][j] + right
            child[(i, j)] = (i+1, j+1)
        
        cache[(i,j)] = result
        return result

def get_path_3(arr, child):
    path = []
    coord = (0, 0)
    while len(path) < len(arr):
        path.append(arr[coord[0]][coord[1]])
        coord = child[coord]

    return path


if __name__ == "__main__":
    arr = [
            [7],
            [3, 8],
            [8, 1, 0],
            [2, 7, 4, 4],
            [4, 5, 2, 6, 5]
        ]

    print(ball_drop_1(arr)[1])
    print(get_path_1(arr, ball_drop_1(arr)[0]))
    print(ball_drop_2(arr)[1])
    print(get_path_2(arr, ball_drop_2(arr)[0]))
    print(ball_drop_3(arr)[1])
    print(ball_drop_3(arr)[0])


