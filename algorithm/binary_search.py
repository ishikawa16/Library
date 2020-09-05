def binary_search(key):
    """二分探索法 O(logN)

    Args:
        key (int): 基準値

    Vars:
        ok (int): 条件を満たすindexの上限値/下限値
        ng (int): 条件を満たさないindexの下限値-1/上限値+1
    
    Returns:
        int: 条件を満たす最小値/最大値
    """
    ok = 5
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2

        if isOK(mid, key):
            ok = mid
        else:
            ng = mid
    
    return ok

def isOK(i, key):
    """条件判定

    Args:
        i   (int): 判定対象の値
        key (int): 基準値

    Returns:
        bool: iが条件を満たすか否か
    """
    return a[i] >= key



'''
<使用例 (配列aにおいて要素が5以上となる最小のindexを求める)>
>>> a = [1, 3, 4, 6, 8, 9]
>>> binary_search(5)
3
'''