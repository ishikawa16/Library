import bisect

def inv_num(a):
    """転倒数 O(NlogN)

    Args:
        a (list): 対象の配列

    Returns:
        int: 配列aの転倒数
    """
    a = compress(a)
    bit = BinaryIndexedTree([0] * len(a))

    res = 0
    for i, v in enumerate(a):
        res += i - bit.query(v+1)
        bit.update(v+1, 1)
    
    return res


# inv_numの実行に必要なクラス/関数
class BinaryIndexedTree:
    """BIT: Binary Indexed Tree

    Attributes:
        n (int):     要素数
        data (list): 要素の格納先 (1-indexed)
    """
    def __init__(self, a):
        """初期化
    
        Args:
            a (list): 対象の配列
        """
        self.n = len(a)
        self.data = [0] * (self.n + 1)
        for i, v in enumerate(a):
            self.update(i+1, v)

    def query(self, i):
        """区間和の計算 O(logN)

        Args:
            i (int): 区間の右端のindex
        
        Returns:
            int: [0, i)の区間和
        """
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        
        return res

    def update(self, i, v):
        """値の更新 O(logN)

        Args:
            i (int): 加算対象のindex+1
            v (int): 加算値
        """
        while i <= self.n:
            self.data[i] += v
            i += i & -i

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
    a = [3, 1, 5, 4, 2]
    print(inv_num(a))