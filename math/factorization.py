def factorization(n):
    """素因数分解 O(√N)

    Args:
        n (int): 対象の値

    Returns:
        list: 素因数とその個数の組み合わせの列挙
    """
    res = []
    m = 2
    while m ** 2 <= n:
        if n % m == 0:
            cnt = 0
            while n % m == 0:
                cnt += 1
                n //= m
            res.append([m, cnt])
        m += 1

    if n > 1:
        res.append([n, 1])

    return res


# Driver Code
if __name__ == "__main__":
    print(factorization(24))
    # [[2, 3], [3, 1]]