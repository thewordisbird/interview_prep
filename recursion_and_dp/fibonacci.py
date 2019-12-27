# determine the fibonacci value for a given numver. Recall fib(n) = fib(n-1) + fib(n-2)

# Recursive example without memoization
def fib(n):
    if n < 2:
        return n

    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    for n in range(10):
        print(f' fib({n}) = {fib(n)}')