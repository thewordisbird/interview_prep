# Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.
# Suppose you triangulate the polygon into N-2 triangles.  For each triangle, the value of that triangle is the product 
# of the labels of the vertices, and the total score of the triangulation is the sum of these values over all N-2 triangles in the triangulation.
# Return the smallest possible total score that you can achieve with some triangulation of the polygon.


# NOTES:
# This is similar to Matrix multiplication since there are sequential splits of the input. The dificulty in this problem
# is that you must maintiain indexes in a circular list. To accomplish this, modding the calculated indexes (j and b) by
# the length of the list will give the circular index. 

def poly_tri(A):
    # Initiate dp table. The table will store the minimum triangulation cost for the polygon (i...j)
    dp = [[0 for x in range(len(A))] for y in range(len(A))]

    # Evaluate the sub problems from smallest to largest to allow them to build on eachother.
    # The g variable represents the gap between i and j.
    for g in range(2, len(A)):
        for i in range(len(A)):
            j = (i + g) % len(A)
            # Set dp to infinity to allow comparison for k evaluations. This could also be done with a min
            # against q, but this would allow for a solution including the splits
            dp[i][j] = float('inf')
            # Look at all sub polygons in (i...j)
            for k in range(1,g):
                b = (i+k)%len(A)
                q = cost(A[i],A[b],A[j]) + dp[i][b] + dp[b][j] 
                if q < dp[i][j]:
                    dp[i][j] = q
    return dp[0][-1]


def cost(a,b,c):
    # Calculate the cost of the triangle. This could be done in the main function
    # But abstracting it allows for simple changes
    return a*b*c

if __name__ == "__main__":
    A = [1,3,1,4,1,5]
    r = poly_tri(A)
    print(r)