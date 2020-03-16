# Text Justification:
# Given text, split the file into "good" lines that minimize excess spacing defined by a badness function for
# a line with max width w.

# Solution Steps:
# 1) Subproblem of optimal substructure: What is the optimal spacing for the suffix of the text, text[i:]
# 
# 2) Guess: Choosing a word at random what needs to be know to decide weather or not to split the line at
#       this point? 
#       - What is the optimal line break before this point to start the badness calculation from
# 
# 3) Recurrence: for every word there are two options:
#       - Add the word to the current line and evaluate the rest of the text
#       - Break the line at this point and start and start a new line
#       DP[i,j] = min(DP[])


def print_neatly(words, n):
    dp = [[0 for j in range(len(words))] for i in range(len(words))]
    b = [[None for j in range(len(words))] for i in range(len(words))]
    for l in range(1, len(words) + 1):
        
        for i in range(len(words) - l + 1):
            j = i + l -1
            print(i,j)
            dp[i][j] = cost(words, n, i, j)
            b[i][j] = j
            q = float('inf')
            x = j
            for k in range(i, j+1):
                c = dp[i][k] + dp[k+1][j]
                if c < q:
                    q = c
                    x = k
            if q < dp[i][j]:
                dp[i][j] = q
                b[i][j] = x
    return dp, b

def cost(words, n, i, j):
    chars = 0
    spaces = j - i
    for x in range(i, j+1):
        chars += len(words[x])
    
    tot_chars = chars+spaces

    if tot_chars <= n:
        return (n - tot_chars) ** 2
    else:
        return float('inf')



if __name__=="__main__":
    sentence = "This is a sentence that needs to be neatly printed"
    words = sentence.split()
    n = 10
    r_a, r_b = print_neatly(words, n)

    for a in r_a:
        print(a)

    print('\n')
    for b in r_b:
        print(b)            

# Trace from i loop for off by 1 issue