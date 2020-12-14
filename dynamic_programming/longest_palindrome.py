def longest_palindrome(str):
    longest = ""
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            tmp_str = str[i:j+1]
            print('evaluating string:', tmp_str)
            if is_palindrome(tmp_str) and j-i > len(longest):
                
                longest = tmp_str
    
    return longest

def longest_palindrome_rec(str, memo = {}):
    if str in memo: return memo[str]
    if len(str) == 1: return str
    if is_palindrome(str): return str
    print('evaluating', str)

    left = longest_palindrome_rec(str[:-1], memo)
    right = longest_palindrome_rec(str[1:], memo)
    if len(left) > len(right):
        memo[str] = left
        return left
    else:
        memo[str] = right
        return right

def is_palindrome(str):
    i = 0
    j = len(str) - 1

    while j >= i:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
        
    return True

if __name__ == "__main__":
    # print(is_palindrome('a'))
    # print(is_palindrome('ab'))
    # print(is_palindrome('abc'))
    # print(is_palindrome('aba'))
    # print(longest_palindrome('banana'))
    # print(longest_palindrome('aabcdcb'))

    print(longest_palindrome_rec('banana'))
    print(longest_palindrome_rec('aabcdcb'))