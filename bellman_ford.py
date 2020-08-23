# Bellman-Ford Algorithm

def bellman_ford(s):
    '''
    始点sから各頂点への最短距離を求める (重み付き有向グラフ)
    O(VE)
    '''
    dist = [float('inf')] * v
    dist[s] = 0

    for i in range(v):
        update = False
        for p, q, cost in edge:
            if dist[p] != float('inf') and dist[q] > dist[p] + cost:
                dist[q] = dist[p] + cost
                update = True
        if not update:
            break
        if i == v - 1:  # 負閉路が存在する場合はFalseを返す
            return False

    return dist


################################
v, e = map(int, input().split())  # v:頂点数, e:辺の数

edge = []  # edge[i]:[始点,終点,重み]
for _ in range(e):
    s, t, d = map(int, input().split())
    edge.append([s, t, d])

print(bellman_ford(0))