def wb(str, dict):
    if len(str) == 0:
        return True
    
    for i in range(1, len(str) + 1):
        print(f'checking {str[:i]} in {dict} -> {str[:i] in dict}')
        if str[:i] in dict:
            return wb(str[i:], dict)

    return False

if __name__ == "__main__":
    d = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}
    s = 'iceream'
    print('running')
    print(wb(s, d))