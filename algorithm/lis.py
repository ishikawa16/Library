import bisect

def lis(a):
    """最長増加部分列 O(NlogN)

    Args:
        a (list): 対象の配列
    
    Returns:
        int: 最長増加部分列の長さ
    """
    l = [a[0]]
    for v in a:
        if l[-1] < v:
            l.append(v)
        else:
            l[bisect.bisect_left(l, v)] = v

    return len(l)



'''
<使用例>
>>> a = [1, 5, 3, 6, 2, 4, 8, 7]
>>> lis(a)
4
'''