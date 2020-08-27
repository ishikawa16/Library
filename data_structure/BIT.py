# BIT: Binary Indexed Tree

def query(i):
    '''
    a[0] + a[1] + … + a[i-1] を求める
    O(logN)
    '''
    res = 0
    while i > 0:
        res += BIT[i]
        i -= i & -i
    
    return res


def update(i, x):
    '''
    a[i-1]にxを加算
    O(logN)
    '''
    while i <= n:
        BIT[i] += x
        i += i & -i



n = 6  # 要素数
a = [1, 3, 5, 2, 6, 4]
BIT = [0] * (n+1)
for i, v in enumerate(a):
   update(i+1, v)

'''
query(5)
> 17

update(3, 2)
query(3)
> 19
'''