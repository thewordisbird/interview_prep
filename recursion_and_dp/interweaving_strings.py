def interweaving_strings(str_a, str_b, str_c):
    # Pre check:
    if len(str_c) != len(str_a) + len(str_b):
        return False

    # Concatenate str_a and str_b
    str = str_a + str_b

    # Check Permutations
    return check_perms(str, str_c)

def check_perms(str, target_string, str_perm=''):
    
    if str_perm == target_string:
        return True
    elif str_perm != target_string[:len(str_perm)] or len(str) == 0:
        return False

    else:
        for i in range(len(str)):
            str_perm = str_perm + str[i]
            if check_perms(str[:i] + str[i+1:], target_string, str_perm):
                    return True
            else:
                # Backtrack before trying next path
                str_perm = str_perm[:-1]
    return False

if __name__ == "__main__":
    str_a = 'aaaaaaa'
    str_b = 'aaaabaaa'
    str_c = 'aaaaaaaaaaaaaab'

    #str_a = 'abcdef'
    #str_b = '12345'
    #str_c = 'abc123def45'

    print(interweaving_strings(str_a, str_b, str_c))
