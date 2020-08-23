# Ex_Euclidean Algorithm

def ex_gcd(a, b):
    '''
    ax + by = gcd(a, b) の整数解を求める
    O(loga)
    '''
    if b == 0:
        return 1, 0
    else:
        x, y = ex_gcd(b, a%b)
        return y, x - (a // b) * y