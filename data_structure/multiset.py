import heapq

class MultiSet:
    """順序付き多重集合

    Attrubutes:
        d (dict):     要素を格納する辞書
        min_q (list): 要素を格納する最小値取得用の優先度付きキュー
        max_q (list): 要素を格納する最大値取得用の優先度付きキュー
    """
    def __init__(self):
        """初期化 O(1)
        """
        self.d = dict()
        self.min_q = []
        self.max_q = []

    def add(self, v):
        """要素の追加 O(logN)

        Args:
            v (int): 追加する要素
        """
        if v not in self.d:
            self.d[v] = 1
        else:
            self.d[v] += 1

        heapq.heappush(self.min_q, v)
        heapq.heappush(self.max_q, -v)

    def remove(self, v):
        """要素の削除 O(logN)

        Args:
            v (int): 削除する要素

        Returns:
            bool: vを削除できるか否か
        """
        if self.exists(v):
            self.d[v] -= 1
        else:
            return False

        while len(self.min_q) > 0:
            if self.d[self.min_q[0]] == 0:
                heapq.heappop(self.min_q)
            else:
                break

        while len(self.max_q) > 0:
            if self.d[-self.max_q[0]] == 0:
                heapq.heappop(self.max_q)
            else:
                break

        return True

    def exists(self, v):
        """要素の存在確認 O(1)

        Args:
            v (int): 判定する要素

        Returns:
            bool: vが存在するか否か
        """
        if v in self.d and self.d[v] > 0:
            return True
        else:
            return False

    def min(self):
        """最小値の取得 O(1)

        Returns:
            int/bool: 最小値 (集合が空の場合はFalse)
        """
        if len(self.min_q) > 0:
            return self.min_q[0]
        else:
            return False

    def max(self):
        """最大値の取得 O(1)

        Returns:
            int/bool: 最大値 (集合が空の場合はFalse)
        """
        if len(self.max_q) > 0:
            return -self.max_q[0]
        else:
            return False


# Driver Code
if __name__ == "__main__":
    ms = MultiSet()

    ms.add(3)              # {3}
    ms.add(1)              # {1, 3}
    ms.add(5)              # {1, 3, 5}
    ms.add(2)              # {1, 2, 3, 5}
    ms.add(4)              # {1, 2, 3, 4, 5}
    print(ms.exists(1))
    # True
    print(ms.min())
    # 1
    print(ms.max())
    # 5

    ms.remove(1)           # {2, 3, 4, 5}
    print(ms.exists(1))
    # False
    print(ms.min())
    # 2