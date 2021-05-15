def mod_comb(n, k, p):
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

def comb_init(n, p):
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


# Driver Code
if __name__ == "__main__":
    max_n = 10000
    mod = 10 ** 9 + 7

    fact = [1]
    fact_inv = [0] * (max_n+1)
    comb_init(max_n, mod)
    print(mod_comb(1000, 500, mod))
    # 159835829