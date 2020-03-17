def lsc(strings):
    # Sort strings from smallest to largest
    strings.sort(key=len)
    

    # Initialize data structures
    dp = {s:-float('inf') for s in strings}
    p = {}

    for string in strings:
        
        if len(string) == 1:
            dp[string] = 0
            p[string] = None

        for k in range(len(string)):
            tmp = string[:k]+ string[k+1:]
            if tmp in p:
                if dp[string] < dp[tmp] + 1:
                    dp[string] = dp[tmp] + 1
                    p[string] = tmp

    return dp, p

def get_chain(dp, p):
    head = None
    length = -float('inf')
    for k,v in dp.items():
        if v > length:
            head = k
    
    chain = []
    s = head
    while p[s] != None:
        chain.append(s)
        s = p[s]
    chain.append(s)
    return chain


if __name__ == "__main__":
    strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]
    strings
    dp, p = lsc(strings)
    print(get_chain(dp, p))