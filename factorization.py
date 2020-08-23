# Prime Factorization

def factorization(n):
    '''
    素因数分解の結果を二次元配列に格納する
    O(√N)
    '''
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


'''
factorization(24)
> [[2, 3], [3, 1]]
'''