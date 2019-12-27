 # Find n factorial recursively. Remember n! = n * n - 1 * n - 2 * ... * 1

def n_factorial(n):
    # Base case: n < = 1 -> 1
    if n <= 1:
        return 1

    else:
        return n * n_factorial(n - 1)
    
if __name__ == "__main__":
    for n in range(10):
        print(n_factorial(n))