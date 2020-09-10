import functools

class SuffixArray:
    """Suffix Array

    Attributes:
        s (str):         対象文字列
        n (int):         sの長さ
        k (int):         ダブリングに用いる変数
        sa (list):       Suffix Array
        rank_sa (list):  k文字の部分文字列の順番 (rank[i]: s[i:i+k]が何番目に小さいか)
        lcp (list):      LCP配列
    """
    def __init__(self, s):
        """初期化

        Args:
            s (str): 対象文字列
        """
        self.s = s
        self.n = len(s)
        self.k = 1
        self.sa = [i for i in range(self.n+1)]
        self.rank_sa = [ord(c) for c in s] + [-1]
        self.lcp = [0] * self.n

    def build_sa(self):
        """Suffix Arrayの構築 O(N(logN)^2)
        """
        tmp_rank_sa = [0] * (self.n+1)
        while self.k <= self.n:
            self.sa.sort(key=functools.cmp_to_key(self.compare_sa))

            tmp_rank_sa[self.sa[0]] = 0
            for i in range(1, self.n+1):
                tmp_rank_sa[self.sa[i]] = tmp_rank_sa[self.sa[i-1]]
                if self.compare_sa(self.sa[i-1], self.sa[i]) < 0:
                    tmp_rank_sa[self.sa[i]] += 1
            for i in range(self.n+1):
                self.rank_sa[i] = tmp_rank_sa[i]
            
            self.k *= 2
        
    def get_sa(self):
        """Suffix Arrayの取得 O(1)

        Returns:
            list: Suffix Array
        """
        return self.sa
    
    def build_lcp(self):
        """LCP配列の構築 O(N)
        """
        rank_lcp = [0] * (self.n+1)
        for i in range(self.n+1):
            rank_lcp[self.sa[i]] = i
        
        h = 0
        for i in range(self.n):
            j = self.sa[rank_lcp[i]-1]
            if h > 0:
                h -= 1
            while j + h < self.n and i + h < self.n:
                if self.s[j+h] != self.s[i+h]:
                    break
                h += 1
            self.lcp[rank_lcp[i]-1] = h
    
    def get_lcp(self):
        """LCP配列の取得 O(1)

        Returns:
            list: LCP Array
        """
        return self.lcp
    
    def is_contain(self, t):
        """文字列検索 O(|T|log|S|)

        Args:
            t (str): 検索対象の文字列
        
        Returns:
            bool: tがsに含まれているか否か
        """
        low, high = 0, self.n
        while high - low > 1:
            mid = (high + low) // 2
            if self.s[self.sa[mid]:self.sa[mid]+len(t)] < t:
                low = mid
            else:
                high = mid
        
        return self.s[self.sa[high]:self.sa[high]+len(t)] == t
    
    def compare_sa(self, i, j):
        """比較関数 O(1)

        Args:
            i (int): 比較対象のindex
            j (int): 比較対象のindex
        
        Returns:
            int: -1 or 1
        """
        if self.rank_sa[i] != self.rank_sa[j]:
            return -1 if self.rank_sa[i] < self.rank_sa[j] else 1
        else:
            rank_ik = (self.rank_sa[i+self.k] if i + self.k <= self.n else -1)
            rank_jk = (self.rank_sa[j+self.k] if j + self.k <= self.n else -1)
            return -1 if rank_ik < rank_jk else 1



'''
<使用例>
>>> s = 'abracadabra'
>>> sa = SuffixArray(s)
>>> sa.build_sa()
>>> sa.get_sa()
[11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
>>> sa.build_lcp()
>>> sa.get_lcp()
[0, 1, 4, 1, 1, 0, 3, 0, 0, 0, 2]
>>> t = 'racad'
>>> sa.is_contain(t)
True
>>> t = 'racab'
>>> sa.is_contain(t)
False
'''