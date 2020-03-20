def lsc(strings):
    # Sort strings from smallest to largest
    strings.sort(key=len)
    

    # Initialize data structures
    dp = {s:-float('inf') for s in strings}
    p = {}

    for string in strings:
        if len(string) == 1:
            dp[string] = 1
            p[string] = None
        
        for k in range(len(string)):
            tmp = string[:k]+ string[k+1:]
            if tmp in p:
                if dp[string] < dp[tmp] + 1:
                    dp[string] = dp[tmp] + 1
                    p[string] = tmp
        if dp[string] < 0:
            dp[string] = 1
            p[string] = None
    return get_chain(dp, p)

def get_chain(dp, p):
    print(dp, p)
    head = None
    length = -float('inf')
    for k,v in dp.items():
        if v > length:
            head = k
            length = v
    
    chain = []
    s = head
    while p[s] != None:
        chain.append(s)
        s = p[s]
    chain.append(s)
    if len(chain) > 1:
        return chain
    else:
        return []


if __name__ == "__main__":
    strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]

    #strings = ['abcdefg', '1234', 'abdefg', 'abdfg', '123', '12', 'bg', 'g', '12345', '12a345']
    print(lsc(strings)) 