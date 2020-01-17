def interweaving_strings(one, two, three):
    if len(one) + len(two) != len(three):
        return False

    return _interweaving_strings(one, two, three)

def _interweaving_strings(str_a, str_b, target, perm=''):
    print(f'_interweaving_strings({str_a}, {str_b}, {target}, {perm})')
    if perm == target:
        return True
    elif perm != target[:len(perm)] or str_a == '' and str_b == '':
        return False
    elif str_a == '':
        _interweaving_strings(str_a, str_b[1:], target, perm + str_b[0])
    elif str_b == '':
        _interweaving_strings(str_a[1:], str_b, target, perm + str_a[0])
    else:
        if _interweaving_strings(str_a[1:], str_b, target, perm + str_a[0]):
            return True
        elif _interweaving_strings(str_a, str_b[1:], target, perm[:-1] + str_b[0]):
            return True
        else:
            return False
    return False

if __name__ == "__main__":
    one = 'abc'
    two = '123'
    three = 'abc123'

    print(interweaving_strings(one,two,three))

    

