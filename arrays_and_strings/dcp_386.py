# Daily Coding Problem #385
# Given a string, sort it in decreasing order based on the frequency of characters. 
# If there are multiple possible solutions, return any of them.

# For example, given the string tweet, return tteew. eettw would also be acceptable.

def sorted_chars_simple(str):
    return ''.join(sorted(str))

def sorted_chars_hard(str):
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return [{k:v} for k,v in char_count]

# Need to figure out data structure for sorting. Maybe try sorting dict?

def merge_sort(lst, start=0, end=None):
    if end == None:
        end = len(lst)
    
    if start < end:
        mid = (start + end) // 2
        merge_sort(lst, start, mid)
        merge_sort(lst, mid + 1, end)
        merge_pointers(lst, start, end)

    else:
        return

    return nums

def merge_pointers(lst, start, end):
    result = []

    left_end = (start + end) // 2
    right_start = left_end - 1
    left_pointer = start
    right_pointer = right_start
    index = left_pointer

    while left_pointer <= left_end and right_pointer <= end:
        if lst[left_pointer] >= lst[right_pointer]:
            result.append(lst[left_pointer])
            left_pointer += 1
        else:
            result.append(lst[right_pointer])
            right_pointer += 1

    # Clear leftovers
    for i in range(left_pointer, left_end):
        result.append(lst[i])

    for j in range(right_pointer, end):
        result.append(lst[j])
    
    # sort nums in place
    for item in result:
        lst[index] = item
        index += 1

    
    

if __name__ == "__main__":
    s = 'tweet'
    print(sorted_chars(s) == 'tteew' or sorted_chars(s) == 'eettw')