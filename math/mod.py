def mod_pow(a, n, p):
    """累乗 O(logN)

    Args:
        a (int): 対象の値
        n (int): 指数
        p (int): 除数

    Returns:
        int: a^n mod p
    """
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % p
        a = a * a % p
        n >>= 1
    return res

def mod_comb_k(n, k, p):
    """二項係数 0(1)

    Args:
        n (int): 添字
        k (int): 添字
        p (int): 除数

    Returns:
        int: nCk mod p
    """
    if n < k or n < 0 or k < 0:
        return 0
    else:
        return fact[n] * fact_inv[k] * fact_inv[n-k] % p

def com_init(n, p):
    """二項係数の計算の前処理 O(N)

    Args:
        n (int): 上限値
        p (int): 除数
    """
    for i in range(n):
        fact.append(fact[-1] * (i+1) % p)

    fact_inv[-1] = pow(fact[-1], p-2, p)
    for i in range(n-1, -1, -1):
        fact_inv[i] = fact_inv[i+1] * (i+1) % p



'''
<使用例>
>>> fact = [1]
>>> fact_inv = [0] * (1000+1)
>>> mod = 10 ** 9 + 7
>>> com_init(1000, mod)
>>> mod_comb_k(1000, 500, mod)
159835829
>>> mod_pow(3, 45, mod)
644897553
'''