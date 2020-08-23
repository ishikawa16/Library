# Warshall-Floyd Algorithm

def warshall_floyd():
    '''
    すべての頂点間の最短距離を求める (重み付き有向グラフ)
    O(V^3)
    '''
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


################################
v, e = map(int, input().split())  # v:頂点数, e:辺の数

dist = [[float('inf')] * v for _ in range(v)]  # dist[i][j]:i → jの重み(存在しない場合はinf, i = jの場合は0)
for _ in range(e):
    s, t, d = map(int, input().split())
    dist[s][t] = d
for i in range(v):
    dist[i][i] = 0

print(warshall_floyd())