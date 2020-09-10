import bisect

def compress(a):
    """1次元座標圧縮 (大小関係の抽出) O(NlogN)

    Args:
        a (list): 対象の配列
    
    Returns:
        list: 圧縮済みの配列
    """
    tmp = sorted(list(set(a)))
    res = []
    for v in a:
        res.append(bisect.bisect_left(tmp, v))
    
    return res


# Driver Code
if __name__ == "__main__":
    a = [1, 4, 3, 4, 8, 6]
    print(compress(a))