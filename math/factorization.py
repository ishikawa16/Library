def factorization(v):
    """素因数分解 O(√N)

    Args:
        v (int): 対象の値

    Returns:
        list: 素因数とその個数の組み合わせの列挙
    """
    res = []
    fact = 2
    while fact ** 2 <= v:
        if v % fact == 0:
            cnt = 0
            while v % fact == 0:
                cnt += 1
                v //= fact
            res.append([fact, cnt])
        fact += 1

    if v > 1:
        res.append([v, 1])

    return res


# Driver Code
if __name__ == "__main__":
    print(factorization(24))
    # [[2, 3], [3, 1]]