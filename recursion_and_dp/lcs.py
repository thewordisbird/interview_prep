def longestCommonSubsequence(str1, str2):
    dp = [[0 for j in range(len(str1))] for i in range(len(str2))]

    for i in range(len(str2)):
        for j in range(len(str1)):
            if str2[i] == str1[j]:
                increase = 1
            else:
                increase = 0

            if i == 0 and j == 0:
                dp[i][j] = increase
            elif i == 0:
                dp[i][j] = max(dp[i][j-1],increase)
            elif j == 0:
                dp[i][j] = max(dp[i-1][j], increase)


            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + increase )
        

    solution = list(reversed(path(str1, str2, dp)))
    print(dp[-1][-1])
    for i in dp:
        print(i)
    return solution

def lcs(str1, str2):
    dp = [[0 for j in range(len(str2) + 1)]for i in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1, 1):
        for j in range(1, len(str2) + 1, 1):
            if str1[i-1] == str2[j-1]:
                increase = 1
            else:
                increase = 0
            
            dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + increase )

    print(dp[-1][-1])

def lcs_path(str1, str2, dp):
    i = len(str1)
    j = len(str2)
    path = []
    while i > 0 and j > 0:
        if str1[i] == str2[j]:
            path.append(str1[i])
            i -= 1
            j -= 1
        


def path(str1, str2, dp):
    i = len(str2) - 1
    j = len(str1) - 1
    
    path = []

    while i > 0 and j > 0:
        if str2[i] == str1[j]:
            path.append(str1[j])
            i -= 1
            j -= 1
        
        else:
            if dp[i][j-1] > dp[i-1][j]:
                j -= 1
            else:
                i -= 1

    if dp[i][j] > 0:
        if i == 0:
            path.append(str2[i])

        else:
            path.append(str1[j])

    return path

if __name__ == "__main__":
    str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str2 = "CCCDDEGDHAGKGLWAJWKJAWGKGWJAKLGGWAFWLFFWAGJWKAGTUV"
    #print(longestCommonSubsequence(str1, str2))
    lcs(str1, str2)

    