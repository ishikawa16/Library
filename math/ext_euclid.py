def ext_euclid(a, b):
    """拡張ユークリッドの互除法 O(loga)

    Args:
        a (int): 対象の値
        b (int): 対象の値

    Returns:
        tuple: ax + by = gcd(a, b) の整数解
    """
    if b == 0:
        return 1, 0
    else:
        x, y = ext_euclid(b, a%b)
        return y, x - (a // b) * y


# Driver Code
if __name__ == "__main__":
    print(ext_euclid(4, 12))
    # (1, 0)