# Rod Cutting
# Problem:
# Given a rod of length n inches and a table of prices pi for i = 1, 2, ... , n-1, n. 
# Determine the maximum revenue rn obtainable by cutting up the rod and selling the pieces.

# Bonus: What will the pieces be?


# Evaluation:
#   Subproblems: ri for all lengths l < n
#   Recurrence: ri = max(p[i-j] + rj for i = 0...n, j = 1...i)
#   Topological Order: Evaluate lengths from smallest to largest

def rod_cut(p):
    # Initialize dp table
    dp = [0 for _ in range(len(p))]
    cuts = [0 for _ in range(len(p))]
    for i in range(1, len(p)):
        q = -float('inf')
        c = 0
        for j in range(i):
            if p[i-j] + dp[j] > q:
                q = p[i-j] + dp[j]
                c = j
        dp[i] = q
        cuts[i] = c
    return dp[-1], get_cut_lengths(cuts)

def get_cut_lengths(cuts):
    lengths = []
    remainder = len(cuts) - 1
    i = cuts[-1]
    
    while i > 0:
        lengths.append(i)
        remainder -= i
        i = cuts[i]

    lengths.append(remainder)
    return lengths

if __name__ == "__main__":
    p= [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(rod_cut(p))
    