# Sieve of Eratosthenes

def eratosthenes(n):
    '''
    n以下の整数の素数判定/素数列挙/最小素因数列挙 (n > 1)
    O(NloglogN)
    '''
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    min_factor = [-1] * (n+1)
    min_factor[0] = 0
    min_factor[1] = 1

    for i in range(2, n+1):
        if is_prime[i]:
            min_factor[i] = i
            for j in range(i*2, n+1, i):
                is_prime[j] = False
                if min_factor[j] == -1:
                    min_factor[j] = i

    # 素数判定
    # return is_prime

    # 素数列挙
    # return [i for i in range(n+1) if is_prime[i]]

    # 最小素因数列挙
    # return min_factor



'''
<素数判定>
eratosthenes(10)
> [False, False, True, True, False, True, False, True, False, False, False]


<素数列挙>
eratosthenes(10)
> [2, 3, 5, 7]


<最小素因数列挙>
eratostenes(10)
> [0, 1, 2, 3, 2, 5, 2, 7, 2, 3, 2]
'''