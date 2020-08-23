# Sieve of Eratosthenes

def eratosthenes(n):
    '''
    n以下の整数の素数判定/列挙 (n > 1)
    O(NloglogN)
    '''
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False

    # 素数判定
    # return is_prime

    # 素数列挙
    # return [i for i in range(n+1) if is_prime[i]]