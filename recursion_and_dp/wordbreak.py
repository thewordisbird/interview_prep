def wb(str, dict):
    # Goal: If all sequences have been found in the dict return true
    if len(str) == 0:
        return True
    
    # Choices: look at all substrings in string
    for i in range(len(str)+1):
        # Constraints: is the substring in the dictionary?
        print(f'checking {str[:i]} in {dict} -> {str[:i] in dict}')
        if str[:i] in dict and wb(str[i:], dict):
            return True

    # No solution
    return False

def wb_dp(str, dict, memo={}):
    print(str)
    if len(str) == 0:
        return True

    if str in memo:
        return memo[str]

    if str in dict:
        memo[str] = True
        return True


    for i in range(len(str)+1):
        # Constraints: is the substring in the dictionary?
        print(f'checking {str[:i]} in {dict} -> {str[:i] in dict}')
        if str[:i] in dict and wb_dp(str[i:], dict): 
            memo[str[i:]] = True
            return True
    
    # No solution
    memo[str] = False
    return False




if __name__ == "__main__":
    d = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}
    s = 'samsamsamsamsam'
    print('Running non-dp')
    print(wb(s, d))
    print('Running dp')
    print(wb_dp(s, d))
    