def eratosthenes(max_v):
    """エラトステネスの篩 O(NloglogN)

    Args:
        max_v (int): 上限値 (> 1)

    Returns:
        list: 問題に応じた返り値
            - 素数判定:      is_prime
            - 素数列挙:      [i for i in range(n+1) if is_prime[i]]
            - 最小素因数列挙: min_factor
    """
    is_prime = [True] * (max_v+1)
    is_prime[0] = False
    is_prime[1] = False
    min_factor = [-1] * (max_v+1)
    min_factor[0] = 0
    min_factor[1] = 1

    for i in range(2, max_v+1):
        if is_prime[i]:
            min_factor[i] = i
            for j in range(i*2, max_v+1, i):
                is_prime[j] = False
                if min_factor[j] == -1:
                    min_factor[j] = i

    return is_prime


# Driver Code
if __name__ == "__main__":
    print(eratosthenes(10))
    # [False, False, True, True, False, True, False, True, False, False, False]