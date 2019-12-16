def palindrome_permutation(str):
    char_count = {}
    for char in str:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    odd_count = 0
    for k,v in char_count.items():
        if v%2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False

    return True

if __name__ == "__main__":
    string = 'tact coa'
    print(palindrome_permutation(string))

    string = 'qqwffeeeedsds'
    print(palindrome_permutation(string))

    string = 'qqwffeeeedsdss'
    print(palindrome_permutation(string))