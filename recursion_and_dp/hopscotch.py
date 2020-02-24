"""
ID: thew0rdisbird
LANG: PYTHON3
TASK: nocross
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=530

def parse(fin):
    schema = list(map(lambda x: int(x), fin.readline().split()))
    R = schema[0]
    C = schema[1]
    K = schema[2]

    return [fin.readline().split() for r in range(R)]
    

def hopscotch(board):
    dp = [[0 for j in range(len(board[i]))] for i in range(len(board))]
    dp[0][0] = 1

    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            dp[i][j] = sum_valid_paths(board, dp, i, j)
    
    return dp[-1][-1]


def sum_valid_paths(board, dp, i, j):
    sum = 0
    for x in range(i):
        for y in range(j):
            if board[x][y] != board[i][j]:
                sum += dp[x][y]
    return sum

if __name__ == "__main__":
    with open('hopscotch.in', 'r') as fin:
        board = parse(fin)

    result = hopscotch(board)

    with open('hopscotch.out', 'w') as fout:
        fout.write(str(result))

    # Note: Doesn't pass all tests on USACO.
    # 5-7 show 'x'
    # 8-15 show 't'