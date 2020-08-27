# Calculations of Modulo

def mod_comb_k(n, k):
    '''
    nCk mod p
    '''
    if n < k or n < 0 or k < 0:
        return 0
    else:
        return fact[n] * fact_inv[k] * fact_inv[n-k] % mod


def mod_pow(a, n):
    '''
    a^n mod p
    '''
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res



n = 100000
mod = 10 ** 9 + 7

# nCk mod p の計算準備
fact = [1]
fact_inv = [0] * (n+1)
for i in range(n):
    fact.append(fact[-1] * (i+1) % mod)
fact_inv[-1] = pow(fact[-1], mod-2, mod)
for i in range(n-1, -1, -1):
    fact_inv[i] = fact_inv[i+1] * (i+1) % mod

'''
mod_comb_k(100000, 50000)
> 149033233

mod_pow(3, 45)
> 644897553
'''