
# This is not the optimal solution. Check algoexperts for details on better solution. For the purpose
# of practicing setting recursive trees and coding it's ok. Optimize on further studing
def powerset(array):
    temp = []
    result = [[]]
    return _powerset(array, temp, result)

def _powerset(array, temp, result):

    for i,n in enumerate(array):
        temp.append(n)
        if sorted(temp) not in result:
            result.append(temp[:])
            _powerset(array[:i] + array[i+1:], temp, result)
        # Backtrack
        temp.pop()

    return result

if __name__ == "__main__":
    array = [1,2,3,4]
    print(powerset(array))
