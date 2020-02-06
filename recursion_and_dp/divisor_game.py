def divisor_game(N):
    cache = {}
    return _divisor_game(N, 0, cache)

def _divisor_game(N, player, cache):
    if N == 1:
        if player == 0:
            cache[(0,0)] = False
            return False
        else:
            return True

    for i in range(1, N):
        if (i, player) in cache:
            return cache[(i, player)]

        if N % i == 0:
            result = _divisor_game(N-i, (player + 1)%2, cache)
            if result:
               return True
            else:
                cache[(N,player)] = False
    return False

if __name__ == "__main__":
    N = 5
    print(divisor_game(N))

