def binary_search():
    """二分探索法 O(logN)

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

        if isOK(mid):
            ok = mid
        else:
            ng = mid

    return ok

def isOK(target):
    """条件判定

    Args:
        target (int): 判定対象の値

    Returns:
        bool: targetが条件を満たすか否か
    """
    return A[target] >= 5


# Driver Code
if __name__ == "__main__":
    A = [1, 3, 4, 6, 7, 9]
    print(binary_search())
    # 3