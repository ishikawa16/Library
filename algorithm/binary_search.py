# Binary Search

def isOK(i, key):
    '''
    問題に応じて返り値を設定
    '''
    return a[i] >= key


def binary_search(key):
    '''
    条件を満たす最小/最大のindexを求める
    O(logN)
    '''
    ok = 6   # 条件を満たすindexの上限値/下限値
    ng = -1  # 条件を満たさないindexの下限値-1/上限値+1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2

        if isOK(mid, key):  # midが条件を満たすか否か
            ok = mid
        else:
            ng = mid
    
    return ok



a = [1, 3, 4, 6, 8, 9]

'''
binary_search(6)
> 3
'''