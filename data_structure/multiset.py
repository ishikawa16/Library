import heapq

class MultiSet:
    """順序付き多重集合

    Attrubutes:
        d (dict): 要素を格納する辞書
        h (list): 要素を格納する優先度付きキュー
    """
    def __init__(self):
        """初期化 O(1)
        """
        self.d = dict()
        self.min_h = []
        self.max_h = []

    def add(self, v):
        """要素の追加 O(logN)

        Args:
            v (int): 追加する要素
        """
        if v not in self.d:
            self.d[v] = 1
        else:
            self.d[v] += 1

        heapq.heappush(self.min_h, v)
        heapq.heappush(self.max_h, -v)

    def remove(self, v):
        """要素の削除 O(logN)

        Args:
            v (int): 削除する要素

        Returns:
            bool: vの削除を実行できたか否か
        """
        if self.is_exist(v):
            self.d[v] -= 1
        else:
            return False

        while len(self.min_h) > 0:
            if self.d[self.min_h[0]] == 0:
                heapq.heappop(self.min_h)
            else:
                break

        while len(self.max_h) > 0:
            if self.d[-self.max_h[0]] == 0:
                heapq.heappop(self.max_h)
            else:
                break

        return True

    def is_exist(self, v):
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

    def get_min(self):
        """最小値の取得 O(1)

        Returns:
            int/bool: 最小値 (集合が空の場合はFalse)
        """
        if len(self.min_h) > 0:
            return self.min_h[0]
        else:
            return False

    def get_max(self):
        """最大値の取得 O(1)

        Returns:
            int/bool: 最大値 (集合が空の場合はFalse)
        """
        if len(self.max_h) > 0:
            return -self.max_h[0]
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
    print(ms.is_exist(1))
    # True
    print(ms.get_min())
    # 1
    print(ms.get_max())
    # 5

    ms.remove(1)           # {2, 3, 4, 5}
    print(ms.is_exist(1))
    # False
    print(ms.get_min())
    # 2