"""
ID: thew0rdisbird
LANG: PYTHON3
TASK: nocross
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=718

def parse(fin):
    ln_ct = 0
    arr_a = []
    arr_b = []
    n = int(fin.readline())
    for i in range(2*n):
        x = int(fin.readline()) 
        if 0 <= i < n:
            arr_a.append(x)
        else:
            arr_b.append(x)

    return arr_a, arr_b
  

def nocross(arr_a,arr_b):
    dp = [[0 for j in range(len(arr_b))] for i in range(len(arr_a))]

    for i in range(len(arr_a)):
        for j in range(len(arr_b)):
            if is_valid(arr_a[i], arr_b[j]):
                connection = 1
            else:
                connection = 0

            if i ==0 and j ==0:
                dp[i][j] = connection
            elif i == 0:
                dp[i][j] = max(dp[i][j-1], connection)
            elif j == 0:
                dp[i][j] = max(dp[i-1][j], connection)
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + connection)
    return dp[-1][-1]


def is_valid(a, b):    
    if abs(a - b) <= 4:
        return True
    return False


if __name__ == "__main__":
    with open('nocross.in', 'r') as fin:
        arr_a, arr_b = parse(fin)
    
    result = nocross(arr_a, arr_b)

    with open('nocross.out', 'w') as fout:
        fout.write(str(result))
    

'''
if __name__=="__main__":
    arr_a = [1,2,3,4,5,6]
    arr_b = [6,5,4,3,2,1]

    print(_nocross(arr_a, arr_b))

'''