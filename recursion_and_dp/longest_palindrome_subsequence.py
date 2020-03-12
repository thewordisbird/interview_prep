def lps(s):
    dp = [[0 for y in range(len(s))] for x in range(len(s))]

    for l in range(1, len(s) + 1):
        for i in range(len(s) - l + 1):
            j = i + l - 1
            if i == j:
                dp[i][j] = 1

            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp

def pal(s, dp):
    chars = ['' for _ in range(dp[0][-1])]
    p_min = 0
    p_max = dp[0][-1] - 1
    i = 0
    j = len(dp[0]) - 1
    
    while p_min <= p_max:
        print(p_min, p_max, i, j, chars)
        if dp[i][j] > dp[i][j-1] and dp[i][j] > dp[i+1][j]:
            chars[p_min] = s[i]
            chars[p_max] = s[i]
            p_min += 1
            p_max -= 1
            i += 1
            j-= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            i += 1
    
    return ''.join(chars)



if __name__ == "__main__":
    s = 'character'
    result = lps(s)
    for r in result:
        print(r)
    palindrome = pal(s, result)
    print(palindrome)