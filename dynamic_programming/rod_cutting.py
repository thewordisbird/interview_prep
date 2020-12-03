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


Evaluation:
1) Determine the subproblem and optimal substructure:
    For any length of pipe the problem of determining the optimal cuts to 
    optimize price remains.

    The evaluation metric for this problem is the price, which will be compared
    using the max function

2) Evaluation options (guess):
    At each step in the evaluation a decisoin needs to be made:
        - Cut the pipe at this location
        - Do not cut the pipe at this location
    
    We need to evaluate all options so we will evaluate the solutions to both
    options and compare them.

3) Determine the recurssion:
    i is the length of the rod being evaluated
    L is the total length 
    dp(i) = max(
                Pi + dp(L - i)      : Make a cut at this length
                dp(i + 1)           : Don't make a cut at this length
                )
    
4) Convert to a bottom up solution:
        The x-axis is the lenght of the total rod
        The y-axis is the length of the cut
        At every cell evaluate the max of the above recursion
        i   |   0   1   2   3   4   5   6   7   8   9   10
        Pi  |   0   1   

            0   1   2   3   4   5   6   7   8   9   10
        0   0   1   5   8   9   10  17  17  20  24  30     
        1   0   1   
        2   0
        3   0
        4   0
        5   0
        6   0
        7   0
        8   0
        9   0
        10  0



