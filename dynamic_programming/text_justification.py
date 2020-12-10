# Text Justification Problem:

# Given text, split the file into "good" lines that minimize excess spacing defined by a badness function for
# a line with max width w.

# Evaluation:
# 1) Determine the subproblem and optimal substructure:
#       For every string we would like to reduce the "badness" as it relates
#       to the line width constraint: The subproblem being, giving str[i,j]
#       determine where the break for the 1st line is

# 2) Guess:
#       In at every word, j for (i+1...n+1) the decision is weather to include
#       the word at j in the same line or start a new line


# 3) Recurrence:
def recursive_solution(words, n, i, memo, new_line):
    if i == len(words)-1:
        return 0
    
    if i in memo:
        return memo[i]

    qi = float('inf')
    si = 0
    print(f'Evaluating starting a line at {i}')
    for j in range(i+1, len(words)):
        badness = recursive_solution(words, n, j, memo, new_line) + cost(words, n, i, j-1)
        if badness < qi:
            qi = badness
            si = j
    print('start new line @: ', si)
    memo[i] = qi
    new_line[i]: si
    return qi

# 4) Topological ordering for bottom up solution:
def bottom_up(words, n):
    dp = [[0 for x in range(len(words) + 1)] for y in range(len(words) + 1)]
    nl = [[0 for x in range(len(words) + 1)] for y in range(len(words) + 1)]

    for i in range(len(words), -1, -1):
        dp[i][i] = cost(words, n, i, i)
        qi = float('inf')
        si = 0
        for j in range(i+1, len(words)):
            # j is the start of a new line
            include = cost(words, n, i, j-1) + dp[i][j]











# Solution Steps:
# 1) Subproblem of optimal substructure: What is the optimal spacing for the suffix of the text, text[i:].
#       If we break the string into to parts at optimal point k, we know that str[i:k] is an optimal solution to 
#       a sub problem as is str[k+1:i]. With this, we can check for each substring length from 1 to the length of
#       the entire string and find the optimal break point for those substrings. We can build on each shorter substring
#       set and get the optimal solution from the solution of the subproblems.
# 
# 2) Guess: Choosing a word at random what needs to be know to decide weather or not to split the line at
#       this point? 
#       - What is the optimal line break before this point to start the badness calculation from
# 
# 3) Recurrence: for every word there are two options:
#       - Add the word to the current line and evaluate the rest of the text
#       - Break the line at this point and start and start a new line
#       DP[i,j] = min(cost[i:j], min(dp[i][k] + dp[k+1][j] for i<=k<=j))
#
# 4) Topological Order: We need to build from smaller sub strings so we need to 
#       evaluate the string from left to right in increasing length sub strings
#
# 5) Solution: Maintain a seprate table of breakpoints for every str[i,j]. 

def text_justification(words, n):
    # Table to store badness values to determine breaks
    dp = [[0 for j in range(len(words))] for i in range(len(words))]
    # Table to store breaks
    b = [[None for j in range(len(words))] for i in range(len(words))]
    
    # Iterate over the number of words to use on each line.
    for l in range(1, len(words) + 1):
        # i is the index of the first word on the line        
        for i in range(len(words) - l + 1):
            # j is the index for the word we are deciding should be added to the
            # current line or where a break should occur.
            j = i + l -1
            dp[i][j] = cost(words, n, i, j)
            b[i][j] = j
            # Store the min badness and the break associated with it
            q = float('inf')
            x = j
            for k in range(i, j):
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
        return (n - tot_chars) ** 3
    else:
        return float('inf')

def print_neatly(words, b):
    i = 0
    str = ""
    while i < len(words):
        k = b[i][-1]
        str = str + " ".join(words[i:k+1]) + '\n'
        i = b[i][-1]+1
    print(str)

if __name__=="__main__":
    sentence = """
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Velit aliquet sagittis id consectetur purus ut. Imperdiet massa tincidunt nunc pulvinar. 
                    Aliquet risus feugiat in ante metus. Porta nibh venenatis cras sed felis eget velit aliquet. Duis ultricies lacus sed turpis tincidunt id aliquet. Pharetra convallis posuere morbi leo urna. Netus et malesuada fames ac turpis. 
                    Volutpat sed cras ornare arcu dui vivamus arcu. Scelerisque varius morbi enim nunc faucibus a pellentesque sit amet. Tristique senectus et netus et malesuada fames. Tempor orci eu lobortis elementum nibh tellus molestie nunc non. 
                    Blandit massa enim nec dui nunc mattis enim ut. Fermentum dui faucibus in ornare. Ornare massa eget egestas purus viverra accumsan in nisl nisi. Dolor sed viverra ipsum nunc aliquet bibendum. Potenti nullam ac tortor vitae purus faucibus ornare. 
                    Egestas dui id ornare arcu odio. Etiam dignissim diam quis enim lobortis scelerisque fermentum dui. Maecenas sed enim ut sem viverra aliquet eget.

                    Ultricies leo integer malesuada nunc vel risus. Habitasse platea dictumst quisque sagittis purus. Nec ultrices dui sapien eget. Praesent tristique magna sit amet purus. Urna condimentum mattis pellentesque id nibh tortor id. 
                    Nec ultrices dui sapien eget mi proin sed libero. Ipsum dolor sit amet consectetur adipiscing elit ut. Lectus arcu bibendum at varius vel pharetra vel turpis nunc. Mi bibendum neque egestas congue quisque egestas. Orci ac auctor augue mauris. 
                    Amet consectetur adipiscing elit duis tristique sollicitudin nibh sit amet. Ut venenatis tellus in metus vulputate eu. Urna et pharetra pharetra massa. Quam adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus. Dolor sed viverra ipsum nunc aliquet bibendum enim. Bibendum est ultricies integer quis.

                    Nascetur ridiculus mus mauris vitae ultricies. Vestibulum lectus mauris ultrices eros in cursus turpis. Neque ornare aenean euismod elementum nisi quis eleifend. Vitae semper quis lectus nulla at volutpat diam ut venenatis. Mauris pharetra et ultrices neque ornare aenean euismod. 
                    Non odio euismod lacinia at quis risus sed. Pulvinar proin gravida hendrerit lectus. Platea dictumst vestibulum rhoncus est pellentesque elit ullamcorper dignissim. Amet est placerat in egestas erat imperdiet sed euismod nisi. Pharetra vel turpis nunc eget lorem dolor sed viverra ipsum. 
                    Sem fringilla ut morbi tincidunt augue interdum velit euismod in. Ut etiam sit amet nisl purus in mollis nunc. Sed libero enim sed faucibus turpis in eu mi. Id nibh tortor id aliquet. Et tortor consequat id porta nibh venenatis cras sed. Ac tortor dignissim convallis aenean et tortor at risus. 
                    Tincidunt id aliquet risus feugiat in ante metus dictum at.

                    Eu feugiat pretium nibh ipsum consequat. Porta lorem mollis aliquam ut porttitor leo a diam sollicitudin. At in tellus integer feugiat. Quis risus sed vulputate odio ut. Non tellus orci ac auctor. Odio tempor orci dapibus ultrices in iaculis. Enim ut tellus elementum sagittis vitae et leo duis ut. 
                    Non tellus orci ac auctor augue mauris. Placerat duis ultricies lacus sed turpis tincidunt. Tortor condimentum lacinia quis vel eros donec ac odio. Ut eu sem integer vitae justo.

                    Sagittis purus sit amet volutpat consequat mauris nunc. Ac ut consequat semper viverra nam libero justo laoreet. Luctus venenatis lectus magna fringilla urna. Vitae semper quis lectus nulla at volutpat diam. Montes nascetur ridiculus mus mauris. 
                    Aliquet lectus proin nibh nisl condimentum. Sed vulputate mi sit amet mauris commodo. Est lorem ipsum dolor sit amet consectetur adipiscing. Nibh sit amet commodo nulla facilisi nullam vehicula. Porttitor eget dolor morbi non arcu risus quis varius quam. 
                    Porttitor leo a diam sollicitudin tempor id eu. Id faucibus nisl tincidunt eget nullam. Interdum varius sit amet mattis. Non nisi est sit amet facilisis magna etiam tempor orci. Interdum velit euismod in pellentesque massa placerat duis ultricies lacus.
                """
    words = sentence.split()
    n = 100
    # r_a, r_b = text_justification(words, n)
    
    # print_neatly(words, r_b)
    
    # # View tables:
    # view = False
    # if view == True:
    #     for a in r_a:
    #         print(a)

    #     print('\n')
    #     for b in r_b:
    #         print(b)    

    short_sentence = """
                    The quick brown fox jumps over the fence and runs away
                """

    s = recursive_solution(short_sentence.split(), 10, 0, {}, {})       
    print(s) 
