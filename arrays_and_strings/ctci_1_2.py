def permutation(str_a, str_b):
    if len(str_a) != len(str_b):
        return False
    
    letter_count_a = {}
    letter_count_b = {}

    for i in range(len(str_a)):
        if str_a[i] not in letter_count_a:
            letter_count_a[str_a[i]] = 1
        else:
            letter_count_a[str_a[i]] += 1
        
        if str_b[i] not in letter_count_b:
            letter_count_b[str_b[i]] = 1
        else:
            letter_count_b[str_b[i]] += 1

    if len(letter_count_a) != len(letter_count_b):
        return False

    for ch in letter_count_a:
        if letter_count_a[ch] != letter_count_b[ch]:
            return False
    
    return True

def permutation_sort(str_a, str_b):
    if len(str_a) != len(str_b):
        return False
    
    a = list(str_a)
    b = list(str_b)

    if sorted(a) == sorted(b):
        return True
    return False

if __name__ == "__main__":
    string_a = 'justin'
    string_b = 'jsutin'
    print(permutation(string_a, string_b))
    print(permutation_sort(string_a, string_b))

    string_a = 'jstin'
    string_b = 'jsutin'
    print(permutation(string_a, string_b))
    print(permutation_sort(string_a, string_b))


    string_a = 'ju stin'
    string_b = 'jsut in'
    print(permutation(string_a, string_b))
    print(permutation_sort(string_a, string_b))


    string_a = 'ju stin'
    string_b = 'jsutin'
    print(permutation(string_a, string_b))
    print(permutation_sort(string_a, string_b))

