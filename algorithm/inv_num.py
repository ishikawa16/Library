import bisect

def inv_num(arr):
    """転倒数 O(NlogN)

    Args:
        arr (list): 対象の配列

    Returns:
        int: 配列arrの転倒数
    """
    compressed = compress(arr)
    bit = BinaryIndexedTree(len(compressed))

    num = 0
    for i, v in enumerate(compressed):
        num += i - bit.get_sum(v+1)
        bit.add(v, 1)

    return num


# inv_numの実行に必要なクラス/関数
class BinaryIndexedTree:
    """BIT: Binary Indexed Tree

    Attributes:
        n (int):     要素数
        data (list): 要素の格納先
    """
    def __init__(self, n):
        """初期化 O(1)

        Args:
            n (int): 要素数
        """
        self.n = n
        self.data = [0] * (n+1)

    def get_sum(self, i):
        """区間和の計算 O(logN)

        Args:
            i (int): 区間の右端のindex

        Returns:
            int: [0, i)の区間和
        """
        range_sum = 0
        while i > 0:
            range_sum += self.data[i]
            i -= i & -i

        return range_sum

    def add(self, i, v):
        """値の更新 O(logN)

        Args:
            i (int): 加算対象のindex
            v (int): 加算値
        """
        i += 1
        while i <= self.n:
            self.data[i] += v
            i += i & -i


def compress(array):
    """1次元座標圧縮 (大小関係の抽出) O(NlogN)

    Args:
        array (list): 対象の配列

    Returns:
        list: 圧縮済みの配列
    """
    tmp = sorted(list(set(array)))
    compressed = []
    for v in array:
        compressed.append(bisect.bisect_left(tmp, v))

    return compressed


# Driver Code
if __name__ == "__main__":
    A = [3, 1, 5, 4, 2]
    print(inv_num(A))
    # 5