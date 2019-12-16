def URLify_long(str):
    l = list(str)
    for i, c in enumerate(l):
        if c == ' ':
            l[i] = '%20'
    return ''.join(l)

def URLify_short(str):
    return ''.join([c if c != ' ' else '%20' for c in str])

if __name__ == "__main__":
    string = 'This is a test'
    print(URLify_long(string))
    print(URLify_short(string))