def badness(words, start_index, end_index, max_width):
    if total_width(words, start_index, end_index) > max_width:
        return float('inf')
    else:
        return (max_width - total_width(words, start_index, end_index)) ** 3

def total_width(words, start_index, end_index):
    #print(start_index, end_index, len(words))
    width = 0
    i = start_index
    while i < end_index:
        width += len(words[i]) + 1
        i += 1
    
    width += len(words[end_index])

    return width

def text_justification(paragraph, max_width):
    i = 0
    j = 1
    words = paragraph.split()
    cache = [[None for i in words] for j in words]
    return _text_justification(words, i, j, max_width, cache)

def _text_justification(words, i, j, max_width, cache):
    print(i,j)
    if j <len(words):
        if cache[i][j] != None:
            return cache[i][j]

        badness_break_i = badness(words, i, j, max_width) + _text_justification(words, j, j + 1, max_width, cache)
        badness_no_break_i = _text_justification(words, i, j+1, max_width, cache)
        #print(f'Comparing {badness_break_i} | {badness_no_break_i} for {i}, {j}')
        if badness_break_i < badness_no_break_i:
            cache[i][j] = badness_break_i
            print(f'returning {badness_break_i}')
            return badness_break_i
        else:
            cache[i][j] = badness_no_break_i
            print(f'returning {badness_no_break_i}')
            return badness_no_break_i
        


if __name__ == "__main__":
    paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." 
    p2 = "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    test ="This is a test."
    print(text_justification(test, 25))