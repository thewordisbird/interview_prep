# Given 2 strings, what is the minimum cost to convert string 1 to string 2 using:
#   - Insert: S'[j] into S[i]
#   - Delete: S[i]
#   - Replace: S[i] with S'[j]

# These operations con be weighted with a cost to modify the outcome depending on the circumstances of the problem at hand.
# For example finding minimum edit distance, each operation would be weighted at a cost of 1. This will return the
# minimum number of changes using those operations
#
# Finding the Levensshtein Edit Distance weights a replacement at a cost of 2 while an insertion and deletion maintain
# a cost of 1.

class Operation:
    def __init__(self):
        self.insert = 1500
        self.delete = 1499
        self.replace = 30000

def edit_distance(str_1, str_2):
    o = Operation()
    dp = [[x * o.delete + y * o.insert for x in range(len(str_1) + 1)] for y in range(len(str_2) + 1)]
    
    print(o.delete, o.insert, o.replace)
    for j in range(1, len(str_1) + 1, 1):
        for i in range(1, len(str_2) + 1, 1):
            dp[i][j] = min( dp[i-1][j] + o.insert, \
                            dp[i][j-1] + o.delete, \
                            dp[i-1][j-1] + (0 if str_1[j-1] == str_2[i-1] else o.replace))
    
    for x in dp:
        print(x)
    return dp[-1][-1]


if __name__ == "__main__":
    #str_1 = 'inte*ntion'
    #str_2 = '*execution'

    str_1 = 'adc'
    str_2 = 'abc'

    print(edit_distance(str_1, str_2))