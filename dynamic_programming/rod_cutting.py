# Rod Cutting Problem

# Given a rod of length n inches and a table of prices pi for i = 1,2,...,n, 
# determine the macimum revenue rn obtainable by cutting up the rod and selling 
# the pieces. Note that id the price pn for a rod of length n is large enough,
# an optimal solution may require no cutting at all.__annotations__

# Example:
# Given the table:

# lenght i |  1   2   3   4   5   6   7   8   9   10
# price Pi |  1   5   8   9   10  17  17  20  24  30

# The result would be:
# A rod of length 10 with a price of 30


# Evaluation:
# 1) Determine the subproblem and optimal substructure:
#     For any length of pipe the problem of determining the optimal cuts to 
#     optimize price remains.

#     The evaluation metric for this problem is the price, which will be compared
#     using the max function

# 2) Evaluation options (guess):
#     At each step in the evaluation a decisoin needs to be made:
#         - Cut the pipe at this location
#         - Do not cut the pipe at this location
    
#     We need to evaluate all options so we will evaluate the solutions to both
#     options and compare them.

# 3) Relate subproblem solutions: Determine the recurssion:
#     i is the length of the rod being evaluated
#     L is the total length 
#     dp(i) = max(
#                 Pk + dp(L - k)      : Make a cut at this length
#                 )
#     for all k (1...i)

def recursive_solution(i, pi):
    ''' Recursive solution to the rod-cutting problem

        Args:
            i (int): Length of the rod.
            pi (dict): Price table.
    '''
    # Base case, rod length of 0
    if i == 0:
        return 0
    
    # all other cases:
    q = -float('inf')
    for k in range(1, i+1):
        # Evaluate the combinations of a cut at each length
        q =  max(
                    q, 
                    pi[k] + recursive_solution(i-k, pi)
                )
    return q

# 4a) Memoize the recursive solution to optimize by avoiding recalculations
def memoized_solution(i, pi, memo):
    ''' Memoized solution to the rod-cutting problem. Adds a memo table
        to keep track of optimal values for each cut lenght to avoid
        recalculation.

        Args:
            i (int): Length of the rod.
            pi(dict): Price table
            memo(dict): Memoization table.
    '''
    # Base case, rod length of 0
    if i == 0:
        return 0

    # check if this length has been calculated in memo table
    if i in memo:
        return memo[i]

    # If it hasn't been calculated, continue with evaluation.
    q = -float('inf')
    for k in range(1, i+1):
        q = max(
                    q,
                    pi[k] + memoized_solution(i-k, pi, memo)
                )
    # Before returning the value, add it to the memo table:
    memo[i] = q
    return q

# 5a) Determine the solution to the problem.
#   At what lengths do we cut the pipe to optimize
class Solution:
    def __init__(self, N, pi):
        self.memo = {}
        self.cut = {}
        self.N = N
        self.pi = pi
    

    def top_down_calculation(self, i):
        ''' Top-Down calculation to the rod-cutting problem. 
        
        Adds a memo table to keep track of optimal values for each cut lenght 
        to avoid recalculation. Adds a cut table to track where each cut is made.

        The solution will be constructed in another function.


            Args:
                i (int): Length of the rod.
                pi(dict): Price table
                s(obj): solution object to hold memo and cut tables
        '''
        # Base case, rod length of 0
        if i == 0:
            return 0

        # check if this lenght has been calculated in memo table
        if i in self.memo:
            return s.memo[i]
        
        # If it hasn't been calculated, continue with evaluation
        q = -float('inf')
        c = 0
        for k in range(1, i+1):
            price = self.pi[k] + self.top_down_calculation(i-k)
            if price > q:
                q = price
                c = k
        # Before returning price value, record the optimal price and cut point 
        # in their tables
        self.memo[i] = q
        self.cut[i] = c
        return q

    def top_down_solution(self):
        ''' Constructs the solution of the problem to determine the optimal cut
            points to maximize profit of rod.

            Args:
                N(int): length of the rod
                s(obj): solution object
        '''
        # Build the memo tables:
        self.top_down_calculation(self.N)
        cuts = []
        l = self.N
        while l > 0:
            cuts.append(self.cut[l])
            l = l - s.cut[l]
        
        return cuts

# 4b) Construct a bottom up solution
def bottom_up(N, pi):
    dp = [0 for x in range(N+1)]
    cut = [0 for x in range(N+1)]

    for i in range(1, N+1):
        q = -float('inf')
        c = 0
        for j in range(1, i+1):
            price = pi[j] + dp[i-j]
            if price > q:
                q = price
                c = j
        dp[i] = q
        cut[i] = c
    
    return dp[N], cut

# 5b) Solve the original problem
def bottom_up_solution(N, cut):
    cuts = []
    l = N
    while l > 0:
        cuts.append(cut[l])
        l = l - cut[l]

    return cuts



if __name__ == "__main__":
    N = 10
    pi = {
        1: 1,
        2: 5,
        3: 4,
        4: 9,
        5: 10,
        6: 17,
        7: 17,
        8: 20,
        9: 24,
        10: 30
    }
    print('Recursive Solution')
    print(f"\t{recursive_solution(N, pi)}")

    print('Memoized Solution')
    print(f"\t{memoized_solution(N, pi, {0:0})}")

    print('Top-Down solution')
    s = Solution(N, pi)
    print(f"\t{s.top_down_solution()}")

    print('Bottom-Up solution')
    dp, cut = bottom_up(N, pi)
    print(f"\t{bottom_up_solution(N, cut)}")
    

    


