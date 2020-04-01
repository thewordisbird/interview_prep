def permutations(input):
    cache = {}
    result = []
    _permutations(input, result, cache)
    return result

def _permutations(input, result, cache):
    if len(input) > 1:
        if input in cache:
            return cache[input]

        for i, char in enumerate(input):
            perm = [char] + _permutations(input[:i] + input[i+1:], result, cache)
            cache[input].append(perm[::])
            

    else:
        cache[input] = input
        
        return [input]

def perms(input):
    dp = [[1 for x in len(input)] for y in len(input)]

    for l in range(3, len(input)):
        for i in range(len(input) - l):
            for j in range()

if __name__=="__main__":
    input = [1, 2, 3]

    print(permutations(input))
