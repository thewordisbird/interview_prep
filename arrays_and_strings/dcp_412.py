# The "look and say" sequence is defined as follows: 
#   beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. 
# The first few terms are as follows:
#
# 1
# 11
# 21
# 1211
# 111221
#
# As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.
#
#Given an integer N, print the Nth term of this sequence.

# The solution runs in O(N * M) wher M is the length of the previous string. As this increases every round it is exponential.

def look_and_say(N):
    ls = [1]
    for _ in range(N):
        
        ls = _look_and_say(ls)
        print(ls)

def _look_and_say(arr):
    result = []
    digit_count = 0
    digit_val = arr[0]

    for val in arr:
    
        if val == digit_val:
            digit_count += 1
        
        else:
            result.extend([digit_count, digit_val])
            digit_val = val
            digit_count = 1

    result.extend([digit_count, digit_val])
    
    return result



if __name__ == "__main__":
    look_and_say(10)
